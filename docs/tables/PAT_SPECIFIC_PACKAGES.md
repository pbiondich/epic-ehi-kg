# PAT_SPECIFIC_PACKAGES

> The PAT_SPECIFIC_PACKAGES table contains information about Patient-Specific Packages. These include the Package ID, Linked Barcode, Linking User, and Link Instant of a Package-Specific Package.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `PSP_IDENT` | VARCHAR |  | The unique identifier for the Patient-Specific Package. |
| 7 | `PSP_LINKED_PACKAGE_NDC_ID` | VARCHAR |  | The unique identifier (.1 item) for the NDC record of the package linked to this Patient-Specific Package. |
| 8 | `PSP_LINKED_PACKAGE_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 9 | `LINKING_USER_ID` | VARCHAR |  | The unique identifier (.1 item) for the EMP record of the user who linked the Patient-Specific Package to this patient. |
| 10 | `LINKING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `LINK_UTC_DTTM` | DATETIME (UTC) |  | The instant the Patient-Specific Package was linked to this patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

