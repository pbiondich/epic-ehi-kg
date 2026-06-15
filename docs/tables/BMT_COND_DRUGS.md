# BMT_COND_DRUGS

> The drugs to be used for conditioning.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique identifier for the blood and marrow transplant treatment regimen. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CONDITIONING_DRUG_C_NAME` | VARCHAR | org | The drugs to use for the conditioning regimen. |
| 6 | `COND_DRUG_DOSAGES` | NUMERIC |  | The dosages for the drugs used in the conditioning regimen. |
| 7 | `DRUG_DISP_QTYUNIT_C_NAME` | VARCHAR | org | The dosage units for the drugs used in the conditioning regimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

