# DENTAL_TREAT_PLAN

> This table contains information about a dental billing plan.

**Primary key:** `TREATMENT_PLAN_ID`  
**Columns:** 20  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `PLAN_DESCRIPTION` | VARCHAR |  | The description of the dental treatment plan. |
| 3 | `PLAN_TYPE_C_NAME` | VARCHAR | org | The category number of the plan type. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 4 | `PLAN_STATUS_C_NAME` | VARCHAR |  | The category number for the plan status. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 5 | `PLAN_CREATION_DATE` | DATETIME |  | The date the dental treatment plan was created. |
| 6 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the guarantor account. This column is frequently used to link to the ACCOUNT table. |
| 7 | `COVERAGE_ID` | NUMERIC | FK→ | In table DENTAL_TREAT_PLAN, the column COVERAGE_ID (DTP/37) has been deprecated. This column has been replaced by column COVERAGE_ID (DTP/45) in table DENTAL_PLAN_COVERAGES To look up the deprecated column's value after the Clarity Compass upgrade, join column DENTAL_TREAT_PLAN.TREATMENT_PLAN_ID to table DENTAL_PLAN_COVERAGES column TREATMENT_PLAN_ID and get the COVERAGE_ID value. |
| 8 | `PRICING_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 9 | `PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `TOTAL_CHARGE_AMOUNT` | NUMERIC |  | The total charge amount for the dental treatment plan. |
| 13 | `PATIENT_AMOUNT` | NUMERIC |  | Patient amount of the dental treatment plan. This is self-pay portion of the total charge amount. |
| 14 | `BANDING_DATE` | DATETIME |  | Banding date for orthodontic treatment. It is used on claim and identifies the date the braces were applied. |
| 15 | `PATIENT_CHG_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 16 | `INSURANCE_CHG_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 17 | `SKIP_PREDETERMINATION_YN` | VARCHAR |  | Flag to indicate that no predetermination claim needs to be sent. |
| 18 | `SOURCE_ESTIMATE_ID` | NUMERIC |  | Represents the Estimate record used to create this dental billing plan, if applicable. |
| 19 | `DTP_USER_STATUS_C_NAME` | VARCHAR | org | Status of a Dental Billing Plan as shown on DTP activity. This may be overridden by end users and can be different from PLAN_STATUS_C, which is the system status of this billing plan. |
| 20 | `REPL_BY_TREATMENT_PLAN_ID` | VARCHAR |  | When a dental billing plan record is replaced, the record that replaced this one will be populated here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

