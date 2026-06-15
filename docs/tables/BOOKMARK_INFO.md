# BOOKMARK_INFO

> This table will extract bookmarks from the HNO database.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAG_EXTERNAL_LOCAL_IDENT` | VARCHAR |  | The locally-assigned unique identifier of the tagged external note. |
| 4 | `TAG_EXTERNAL_SOURCE_DXR_CSN_ID` | NUMERIC |  | The ID of the tagged note's source DXR contact. |
| 5 | `TAG_EXTERNAL_ENC_START_DTTM` | DATETIME (Local) |  | The start instant of the encounter associated with the tagged external note. |
| 6 | `TAG_EXTERNAL_ENC_END_DTTM` | DATETIME (Local) |  | The end instant of the encounter associated with the tagged external note. |
| 7 | `TAG_EXTERNAL_ENC_TYPE_C_NAME` | VARCHAR | org | The mapped encounter type ID of the encounter associated with the tagged external note. |
| 8 | `TAG_EXTERNAL_ENC_TYPE` | VARCHAR |  | The free-text encounter type name of the encounter associated with the tagged external note. |
| 9 | `TAG_EXTERNAL_ENC_REF_IDENT` | VARCHAR |  | The reference ID of the encounter associated with the tagged external note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

