# OUT_MED_ADHERE_ACTION_LOG

> This table stores an audit of user actions taken on Value-Based medication adherence care gap dispenses.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OUTCOME_KEY_MED_ACT_LOG` | INTEGER |  | This item stores the outcome's key. This key is unique for an outcome on a particular RDI record. This item is used to link the current outcomes group (I RDI 42010) with the med adherence data stored here. |
| 4 | `OUTCOME_MED_NAME_ACT_LOG` | VARCHAR |  | The name of the medication that action was taken upon. |
| 5 | `OUTCOME_MED_ACT_LOG_NDC_ID` | VARCHAR |  | The networked NDC record ID. |
| 6 | `OUTCOME_MED_ACT_LOG_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 7 | `OUT_MED_LAST_FILL_ACT_LOG_DATE` | DATETIME |  | The fill date for the medication. |
| 8 | `OUT_MED_DAYS_SUPPLY_ACT_LOG` | INTEGER |  | The number of days that the medication fill should last if taken as prescribed. |
| 9 | `OUT_MED_ACT_LOG_ACT_TYPE_C_NAME` | VARCHAR |  | The type of action taken on this dispense. |
| 10 | `OUT_MED_ACT_LOG_UTC_DTTM` | DATETIME (UTC) |  | The instant the action was taken. |
| 11 | `OUTCOME_MED_ACT_LOG_USER_ID` | VARCHAR |  | The user that took the action on the dispense. |
| 12 | `OUTCOME_MED_ACT_LOG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

