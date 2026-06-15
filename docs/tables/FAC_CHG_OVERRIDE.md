# FAC_CHG_OVERRIDE

> Scoring system information for emergency department level of service calculations.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the deployment owner for this contact. |
| 5 | `FAC_CHG_CALC_SCR` | INTEGER |  | Stores the calculated points for the ED facility charge scoring system. |
| 6 | `FAC_CHG_OVR_SYS_SCR` | INTEGER |  | The user-entered score for the facility charge calculation. This overrides the calculated value during calculation of the charge level. |
| 7 | `FAC_CHG_OVR_USR_ID` | VARCHAR |  | The ID of the last user to override the facility charge calculator score. |
| 8 | `FAC_CHG_OVR_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `FAC_CHG_OVR_INST` | DATETIME (Local) |  | The instant of the last facility charge calculation score. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

