
import boto3
import csv
import io
from urllib.parse import unquote_plus

s3 = boto3.client("s3")

def calculate_bonus(salary):
    return int(salary * 0.10)

def lambda_handler(event, context):
    print("Lambda function started!")

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])

        print(f"Reading: s3://{bucket}/{key}")

        # EXTRACT: Read original CSV from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read().decode("utf-8-sig")

        cleaned_content = "\n".join(
            line for line in content.splitlines()
            if line.strip()
        )

        reader = csv.DictReader(io.StringIO(cleaned_content))
        employees = list(reader)

        # TRANSFORM: Add annual bonus (10% of salary)
        for employee in employees:
            salary = int(employee["salary"])
            employee["annual_bonus"] = calculate_bonus(salary)

        # LOAD: Convert processed records back into CSV
        output = io.StringIO()
        fieldnames = [
            "id", "name", "department",
            "salary", "annual_bonus"
        ]

        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)

        # Save processed CSV to S3
        output_key = "processed/" + key.split("/")[-1]

        s3.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=output.getvalue().encode("utf-8"),
            ContentType="text/csv"
        )

        print(f"Total employees: {len(employees)}")
        print(f"Saved: s3://{bucket}/{output_key}")

    return {
        "statusCode": 200,
        "body": "ETL pipeline completed successfully"
    }
