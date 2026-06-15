# MAR_ADMIN_EDITD

> This table contains the original data of medication administrations that have been edited. The data is no longer a current representation of the MAR, but can be used for reporting purposes.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 51  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `SCHEDULED_TIME` | DATETIME (Local) |  | The scheduled time on the MAR. |
| 4 | `EDITED_LINE` | INTEGER |  | The line number of the previously saved data for this administration. |
| 5 | `TAKEN_TIME` | DATETIME (Local) |  | The user-specified time that the action took place. |
| 6 | `SAVED_TIME` | DATETIME (Local) |  | The instant the medication administration was saved. |
| 7 | `EDITD_MAR_ACTION_C_NAME` | VARCHAR | org | The medication administration record (MAR) action category number for the administration. |
| 8 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user that took action on the administration. |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `SEC_USER_ID` | VARCHAR |  | The unique ID of the secondary user associated with this administration. |
| 11 | `SEC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `EDIT_MAR_DOC_USR_ID` | VARCHAR |  | User ID of the user who documented the medication administration. This item is null unless the administering user (ORD 12120) is different than the documenting user. |
| 13 | `EDIT_MAR_DOC_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `SIG` | VARCHAR |  | The dose value of the administration. |
| 15 | `ROUTE_C_NAME` | VARCHAR | org | The route category number for the administration. |
| 16 | `COMMENTS` | VARCHAR |  | The comment associated with the administration. |
| 17 | `REASON_C_NAME` | VARCHAR | org | The reason category number for the administration. A reason is generally required for the actions of Missed and medication administration record hold (MAR Hold), but can be configured for any action. |
| 18 | `SITE_C_NAME` | VARCHAR | org | The site category number for the administration. |
| 19 | `INFUSION_RATE` | VARCHAR |  | The rate at which the medication was infused. |
| 20 | `EDIT_MAR_RATEUNIT_C_NAME` | VARCHAR | org | The infusion rate unit category number for the administration. |
| 21 | `DOSE_UNIT_C_NAME` | VARCHAR |  | The dose unit category number for the administration. |
| 22 | `EDITD_MAR_DURATION` | VARCHAR |  | The length of time the administration took to complete or infuse. |
| 23 | `EDITD_DUR_UNIT_C_NAME` | VARCHAR |  | The duration unit category number for the administration. |
| 24 | `EDIT_MAR_IMM_LNK_ID` | NUMERIC |  | The unique ID of the linked immunization that is associated with this administration. |
| 25 | `EDITD_DUE_ACTION_C_NAME` | VARCHAR |  | The scheduled Medication administration record (MAR) action at a due time category number for the administration. This column will only be populated if Duration-Based Due Actions are configured (LSD 34640 and 34641). |
| 26 | `EDITED_MAR_BILL_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 27 | `EDIT_BLOOD_INFO_LN` | INTEGER |  | This item stores the line pointer to the blood information, for this edit (ORD 13000). |
| 28 | `EDITED_CYCLIC_RATE_PARENT_LINE` | INTEGER |  | The line number of the parent administration of this cyclic rate change due time. |
| 29 | `EDITED_ORIGINAL_AMOUNT` | VARCHAR |  | Edit history of the original amount if weight-based dose conversion or other unit conversion took place. |
| 30 | `EDITED_ORIGINAL_UNIT_C_NAME` | VARCHAR |  | Edited value of the original unit |
| 31 | `EDIT_CUP_IDENT` | VARCHAR |  | This is the ID that dictates which cup an administration belongs to. |
| 32 | `EDITED_SCHEDULED_DOSE` | VARCHAR |  | The dose that was scheduled to be due for the administration of an order with multiple possible doses. |
| 33 | `EDITED_SCHEDULED_DOSE_UNIT_C_NAME` | VARCHAR |  | The scheduled dose unit category ID for the administration. |
| 34 | `EDITED_CONCENTRATION` | VARCHAR |  | The concentration for the administration. |
| 35 | `EDITED_DUR_BASED_PARENT_LINE` | INTEGER |  | The line number of the administration that created this duration-based due time. |
| 36 | `EDITED_DUR_BASED_CHILD_LINE` | INTEGER |  | The line number of the duration-based due time administration that was created by this administration. |
| 37 | `EDITED_CYCLIC_RATE_CHILD_LINE` | INTEGER |  | The line number of the following child administration of this cyclic rate change due time. |
| 38 | `EDITED_SCHEDULED_AMOUNT` | VARCHAR |  | Scheduled administration amount when the order has multiple doses. |
| 39 | `EDITED_SCHEDULED_AMOUNT_UNIT_C_NAME` | VARCHAR |  | Scheduled administration amount unit when the order has multiple doses. |
| 40 | `EDITED_MAR_PEND_USER_ID` | VARCHAR |  | The unique ID of the user with deferred signoff for the administration. |
| 41 | `EDITED_MAR_PEND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `EDITED_MAR_PEND_SECOND_USER_ID` | VARCHAR |  | The unique ID of the verifying user with deferred signoff for the administration. |
| 43 | `EDITED_MAR_PEND_SECOND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 44 | `EDIT_TCI_CONCENTRATION` | VARCHAR |  | Edited target concentration of the TCI pump |
| 45 | `EDIT_TCI_CONCENTRATION_UNIT_C_NAME` | VARCHAR |  | Edited target concentration unit of the TCI pump |
| 46 | `EDIT_TCI_MODEL_C_NAME` | VARCHAR | org | Edited model used for the TCI pump |
| 47 | `EDIT_TCI_TARGET_C_NAME` | VARCHAR | org | Edited TCI Target for a TCI Target |
| 48 | `EDIT_MAR_PSP_IDENT` | VARCHAR |  | This is the identifier that dictates which Patient-Specific Package belongs to an administration. This can also be a comma delimited list of identifiers if multiple patient-specific packages are scanned for a single administration. |
| 49 | `EDIT_MAR_DUAL_SIGN_SOURCE_C_NAME` | VARCHAR |  | The source of the device the second signer used when approving the administration. For example, whether their signoff took place from a remote location |
| 50 | `EDIT_PEND_DUE_ACTION_C_NAME` | VARCHAR |  | Audit trail - the MAR action that was being documented when the administration pended. |
| 51 | `EDIT_DUR_BASED_PARENT_ORDER_ID` | NUMERIC |  | For a duration-based child administration, this item stores the order ID of its parent. When the duration-based parent and child administrations are on the same order, this item is null. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

