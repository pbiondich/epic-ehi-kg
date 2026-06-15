# OR_LOG_ALL_PROC

> The OR_LOG_ALL_PROC table contains OR management system log procedures.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log referred to by this procedure. |
| 2 | `LINE` | INTEGER | PK | The number of the line of procedure in the surgical log. |
| 3 | `OR_PROC_ID` | VARCHAR | FK→ | The unique ID of the procedure. |
| 4 | `OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 5 | `POS_C_NAME` | VARCHAR | org | The category value which represents the patient’s body position during the surgery in the surgical log. |
| 6 | `ANES_TYPE_C_NAME` | VARCHAR | org | The category value which represents the types of anesthesia needed for the surgery in the surgical log. |
| 7 | `LRB_C_NAME` | VARCHAR | org | The category value which represents what section of the body the surgery in the surgical log was performed on. |
| 8 | `OP_REG_C_NAME` | VARCHAR | org | The category value which represents what region of the body will be operated on during the surgery in the surgical log. |
| 9 | `WND_CLS_C_NAME` | VARCHAR | org | The category value which represents the wound class of the patient in the surgical log. |
| 10 | `WND_LOC_C_NAME` | VARCHAR |  | The category value which represents the body location of the wound on the patient in the surgical log. |
| 11 | `ALL_APPROACH_C_NAME` | VARCHAR | org | The category value which represents the approach to the wound. |
| 12 | `ALL_PROCS_TOT_TIME` | INTEGER |  | The total time of all procedures in the log. |
| 13 | `ALL_PROCS_PANEL` | INTEGER |  | The number of the panel in which this procedure was performed. |
| 14 | `COMMENTS` | VARCHAR |  | The free text comments for this procedure. |
| 15 | `RESOURCE_PREF_ID` | VARCHAR |  | Stores the procedure/preference id which was used to default resources (staff, equipment, etc.) corresponding to this procedure. |
| 16 | `RESOURCE_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 17 | `PICKLIST_PREF_ID` | VARCHAR |  | Stores the procedure/preference id whose pick list was copied to create the corresponding pick list for this procedure in the case. |
| 18 | `PICKLIST_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 19 | `MATCHED_PREF_ID` | VARCHAR |  | Stores the preference card that has been selected to override the defaulted preference card. NOTE: Starting in the Epic 2012 release, this column will display the ID of the selected preference card even though the column name says Matched Pref. The ID of the preference card that is matched or defaulted will be stored in I ORL 2018. |
| 20 | `MATCHED_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 21 | `DBC_EPISODE_ID` | NUMERIC |  | Stores the Diagnosis Behandling Combinatie (DBC) episode associated with the current procedure. Used in billing. |
| 22 | `PROC_EAP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 23 | `ALL_PROC_AS_ORDERED` | VARCHAR |  | Denotes the procedure name as exactly ordered by the surgeon/provider. |
| 24 | `ALL_DEF_OR_PROC_ID` | VARCHAR |  | Stores the defaulted preference card. |
| 25 | `ALL_DEF_OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 26 | `ALL_PROC_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 27 | `ALL_PROCS_INCISION_CLOSURE_C_NAME` | VARCHAR |  | The category value of the incision closure associated with the procedure. |
| 28 | `ALL_PANEL_ADDL_ID` | NUMERIC |  | Stores the pointer to the procedure additional data record for all panels. |
| 29 | `ALL_PANEL_ORDER_ID` | NUMERIC |  | This item stores the order ID for the procedure request associated with the log created for the procedure plan case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_PROC_ID` | [OR_PROC](OR_PROC.md) | sole_pk | high |

