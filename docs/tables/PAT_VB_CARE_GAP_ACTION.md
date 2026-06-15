# PAT_VB_CARE_GAP_ACTION

> This table contains data about actions taken by providers on care gap alerts for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `VB_HM_CARE_GAP_TYPE_C_NAME` | VARCHAR |  | This item stores the care gap type for the value-based care gap that was acted on. |
| 5 | `VB_CARE_GAP_ACTION_C_NAME` | VARCHAR |  | This item stores the action taken on a value-based care gap. |
| 6 | `VB_CARE_GAP_ACTION_INST_DTTM` | DATETIME (UTC) |  | This item stores the instant that a user acted on a value-based care gap. |
| 7 | `VB_CARE_GAP_END_INST_DTTM` | DATETIME (UTC) |  | This item stores the instant a value-based care gap action expires. |
| 8 | `VB_CARE_GAP_USER_ID` | VARCHAR |  | This item stores the user who acted on the value-based care gap. |
| 9 | `VB_CARE_GAP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `VB_CARE_GAP_ALERT_CSN_ID` | NUMERIC |  | This item stores the ALT CSN associated with the value-based care gap action. |
| 11 | `VB_CARE_GAP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

