# PAT_ENC_BILLING_ENC

> This table contains encounter-specific data related to Billing Encounters.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 4 | `POS_TYPE_OVRIDE_C_NAME` | VARCHAR | org | Place of service type override for Billing Encounters. If empty, the place of service type is determined by the type set in the facility record (EAF) contained in the Visit Place of Service (I EPT 5617). |
| 5 | `BILL_ENC_IS_VOID_YN` | VARCHAR |  | Indicates whether a Billing Encounter has been marked as voided. For example, if a user creates a Billing Encounter for a patient in error, the user can correct that error by marking the Billing Encounter as voided. |
| 6 | `BILLING_ENC_TYPE_C_NAME` | VARCHAR |  | The type of billing encounter this represents for an encounter of type 99-Billing Encounter. Among other things, this informs how the encounter date is determined. |
| 7 | `BILLING_ENC_START_DATE` | DATETIME |  | The start date of a multi-day billing encounter. |
| 8 | `BILLING_ENC_END_DATE` | DATETIME |  | The end date of a multi-day billing encounter. |
| 9 | `PBX_ENC_STATUS_C_NAME` | VARCHAR |  | Status of a Professional Billing Exchange type encounter. |
| 10 | `PBX_ENC_SRC_ORGANIZATION_ID` | NUMERIC |  | The originating care organization of a Professional Billing Exchange encounter. |
| 11 | `PBX_ENC_SRC_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

