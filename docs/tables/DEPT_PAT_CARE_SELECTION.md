# DEPT_PAT_CARE_SELECTION

> Table containing Department of Patient Care, and Department of Patient Care selection information for orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DPCAR_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `DPCAR_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number (CSN) of the encounter from which the department of patient care (I ORD 77910) was chosen. The last line contains the CSN corresponding to the current department of care, while previous lines contain historical values. |
| 5 | `DPCAR_SEL_LOGIC_C_NAME` | VARCHAR |  | Stores the selection logic used to determine the department of patient care (I ORD 77910) chosen for the order. The last line contains the selection logic that corresponds to the current department of care, while previous lines contain historical values. |
| 6 | `DPCARE_SEL_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant in which the department of patient care (I ORD 77910) was saved for the order. The last line contains the instant in which the current department of care was saved, while previous lines contain historical values. |
| 7 | `DPCARE_UPDT_USER_ID` | VARCHAR |  | Stores the user ID of the user who caused the department of patient care (I ORD 77910) to be saved for the order. Saving of the department of patient care occurs when initially signing an order, when updating the order's authorizing or ordering provider, or when changing the encounter department for the encounter in which the order was signed. The last line contains user ID of the user who triggered the saving of the current department, while previous lines contain historical values. |
| 8 | `DPCARE_UPDT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DPCAR_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

