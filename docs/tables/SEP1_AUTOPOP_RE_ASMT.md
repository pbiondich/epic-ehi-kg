# SEP1_AUTOPOP_RE_ASMT

> This table contains autopopulation data source information for the repeat volume status and tissue perfusion assessment performed data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASMT_YN` | VARCHAR |  | The value (either 0-No or 1-yes) to indicate if a repeat volume status and tissue perfusion assessment was documented. |
| 4 | `NOTE_ID` | VARCHAR | shared | The ID of the note that contains the earliest documentation of repeat volume status and tissue perfusion assessment. |
| 5 | `NOTE_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the note that contains the earliest documentation of repeat volume status and tissue perfusion assessment. |
| 6 | `ORDER_ID` | NUMERIC | shared | The ID of the order (ORD ID) that contains the earliest documentation of repeat volume status and tissue perfusion assessment. |
| 7 | `FLO_MEAS_ID` | VARCHAR | FK→ | The ID of the flowsheet row where repeat volume status and tissue perfusion assessment is documented. |
| 8 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

