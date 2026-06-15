# OR_CASE_ALL_PROC

> The OR_CASE_ALL_PROC table contains OR management system case procedures.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the procedure within the case. |
| 3 | `OR_PROC_ID` | VARCHAR | FK→ | The unique ID of the procedure record. |
| 4 | `OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 5 | `POS_C_NAME` | VARCHAR | org | The category value which represents the position in which the patient should be placed when performing the surgery. |
| 6 | `LRB_C_NAME` | VARCHAR | org | The category value which represents the side of the body the procedure on which the procedure is being performed. |
| 7 | `ANES_TYPE_C_NAME` | VARCHAR | org | The category value which represents the type of anesthesia used for this procedure. |
| 8 | `OP_REG_C_NAME` | VARCHAR | org | The category value which indicates the region of the body that will be operated on during the surgery. |
| 9 | `TOTAL_LENGTH` | INTEGER |  | The total amount of time required for the case. This includes all procedures in all panels as well as the setup and cleanup times for the case. |
| 10 | `PANEL` | INTEGER |  | The procedure panel within which this procedure is contained. This is a numeric value between 1 and 5. |
| 11 | `COMMENTS` | VARCHAR |  | The free text comments for this procedure. |
| 12 | `DEFAULTED_LENGTH` | NUMERIC |  | The length defaulted for this procedure by the system in minutes. |
| 13 | `RESOURCE_PREF_ID` | VARCHAR |  | The procedure or preference card ID used to default the resources in the case for this procedure. |
| 14 | `RESOURCE_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 15 | `PICKLIST_PREF_ID` | VARCHAR |  | The procedure or preference card ID used to default the pick list in the case for this procedure. |
| 16 | `PICKLIST_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 17 | `LENGTH_MODIFIED_YN` | VARCHAR |  | Indicates whether the procedure length was modified by the user. Y indicates that the procedure length was modified. A null value indicates that the length was not modified. An N will not be populated for this column. |
| 18 | `MATCHED_PREF_ID` | VARCHAR |  | This item stores the preference card that has been selected to override the defaulted preference card. |
| 19 | `MATCHED_PREF_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 20 | `POSSIBLE_PROC_YN` | VARCHAR |  | Indicates whether the procedure was flagged as a possible procedure. Y indicates that the procedure was flagged as a possible procedure. N or null indicates that the procedure was not flagged as a possible procedure. |
| 21 | `DBC_EPISODE_ID` | NUMERIC |  | Stores the Diagnose Behandel Combinatie (DBC) episode associated with the current procedure. Used in billing. |
| 22 | `PROC_EAP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 23 | `ALL_PROC_AS_ORDERED` | VARCHAR |  | Specify the procedure name as exactly ordered by the surgeon/provider. |
| 24 | `ALL_PROC_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 25 | `ALL_DEF_OR_PROC_ID` | VARCHAR |  | This item stores the defaulted preference card. |
| 26 | `ALL_DEF_OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 27 | `ALL_PANEL_ADDL_OPE_ID` | NUMERIC |  | Stores the pointer to the procedure additional data record for all panels. |
| 28 | `ALL_PANEL_ORDER_ID` | NUMERIC |  | This item stores the order ID for the procedure request associated with the procedure plan case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |
| `OR_PROC_ID` | [OR_PROC](OR_PROC.md) | sole_pk | high |

