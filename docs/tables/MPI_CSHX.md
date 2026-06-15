# MPI_CSHX

> Table contains history information for the Identity visit IDs.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `MPI_CSHX_ID` | VARCHAR |  | The patient's historical visit identifiers. |
| 7 | `MPI_CSHX_INSTA_DTTM` | DATETIME (Local) |  | Identity audit trail instant for the patient visit ID. |
| 8 | `MPI_CSHX_ID_TYPE_ID` | NUMERIC |  | Identity audit trail ID type for the patient visit ID. |
| 9 | `MPI_CSHX_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 10 | `MPI_CSHX_USER_ID` | VARCHAR |  | Identity audit trail user for the patient visit ID. |
| 11 | `MPI_CSHX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `MPI_CSHX_AUDT_TYP_C_NAME` | VARCHAR |  | Identity audit trail type for the patient visit ID. |
| 13 | `MPI_CSHX_NEW_ID` | VARCHAR |  | Identity audit trail new ID for the patient visit ID. |
| 14 | `MPI_CSHX_DOTONE` | VARCHAR |  | Identity audit trail ID for the patient visit ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

