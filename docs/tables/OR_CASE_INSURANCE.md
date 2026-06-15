# OR_CASE_INSURANCE

> Contains information about patient's case insurance information.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INS_FILING_ORDER_C_NAME` | VARCHAR | org | This item identifies the patient's insurance as primary, secondary, or tertiary. |
| 4 | `INS_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 5 | `INS_PRODUCT_TYPE_C_NAME` | VARCHAR | org | This item contains the patient's insurance product type. |
| 6 | `INS_SUBSCRIBER_NUM` | VARCHAR |  | This item contains the patient's insurance subscriber ID. |
| 7 | `INS_SUBSCR_DOB_DT` | DATETIME |  | This item contains the patient's insurance subscriber date of birth. |
| 8 | `INS_POLICY_NUM` | VARCHAR |  | This item contains the patient's insurance policy number. |
| 9 | `INS_GROUP_NUM` | VARCHAR |  | This item contains the patient's insurance group number. |
| 10 | `INS_PRECERT_NUM` | VARCHAR |  | This item contains the patient's insurance pre-cert number |
| 11 | `INS_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 12 | `INS_SUBSCRIBER_REL_C_NAME` | VARCHAR | org | Describes the Insurance Subscriber Relationship. |
| 13 | `INS_PHONE_NUM` | VARCHAR |  | Contains the phone number for insurance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

