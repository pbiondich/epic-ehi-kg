# ORDER_DX_PROC

> The ORDER_DX_PROC table enables you to report on the diagnoses associated with procedures ordered in clinical system. Since one procedure order may be associated with multiple diagnoses, each row in this table is one procedure - diagnosis relation. We have also included patient and contact identification information for each record. Note that system settings may or may not require that procedures be associated with diagnoses. This table contains only information for those procedures and diagnoses that have been explicitly associated. Check with your clinical system Application Administrator to determine how your organization has this set up.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this procedure record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DX_QUALIFIER_C_NAME` | VARCHAR | org | The diagnosis qualifier category ID, which indicates modifier information for the diagnosis associated with the order record. |
| 7 | `COMMENTS` | VARCHAR |  | Comments added when the procedure was ordered |
| 8 | `DX_CHRONIC_YN` | VARCHAR |  | Indicates whether the diagnosis associated with this order record was marked as chronic during the ordering process. 'Y' indicates that a the diagnosis was marked as chronic. 'N' or NULL indicate that a the diagnosis was not marked as chronic. |
| 9 | `ASSOC_DX_DESC` | VARCHAR |  | This column stores a free text diagnosis description entered by the end user. Also referred to as the "display as" field. |
| 10 | `ASSOC_REQ_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

