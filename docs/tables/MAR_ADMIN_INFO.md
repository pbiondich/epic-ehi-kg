# MAR_ADMIN_INFO

> This table contains the currently active medication administration data. This includes all scheduled and acted upon administrations currently showing on the MAR.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 67  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `TAKEN_TIME` | DATETIME (Local) |  | The user-specified time that the action took place. |
| 4 | `MAR_ORIG_DUE_TM` | DATETIME (Local) |  | The original due time for the administration. |
| 5 | `SCHEDULED_TIME` | DATETIME (Local) |  | The scheduled time on the MAR. |
| 6 | `SAVED_TIME` | DATETIME (Local) |  | The instant the medication administration was saved. |
| 7 | `MAR_SCHD_DTTM` | DATETIME (Local) |  | The instant the original due time was created by the scheduler. This item is not populated for data saved by a user, including user-created due times. |
| 8 | `MAR_ACTION_C_NAME` | VARCHAR | org | The MAR action category number associated with this administration. |
| 9 | `MAR_UNIT_NUM` | VARCHAR |  | The blood unit number associated with this administration. |
| 10 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user that took action on the administration. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `SEC_USER_ID` | VARCHAR |  | The unique ID of the secondary user associated with this administration. |
| 13 | `SEC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `MAR_DOC_USER_ID` | VARCHAR |  | User (EMP) ID of the user who documented the med administration. This item is null unless the administering user (ORD 11110) is different than the documenting user. |
| 15 | `MAR_DOC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `SIG` | VARCHAR |  | The dose value of the administration. |
| 17 | `ROUTE_C_NAME` | VARCHAR | org | The route category number associated with this administration. |
| 18 | `COMMENTS` | VARCHAR |  | The comment associated with the administration. |
| 19 | `REASON_C_NAME` | VARCHAR | org | The category ID of the reason that is given for documenting a certain action. A reason is generally required for the actions of Missed and MAR Hold, but can be configured for any action. |
| 20 | `SITE_C_NAME` | VARCHAR | org | The site category number used for the administration. |
| 21 | `INFUSION_RATE` | VARCHAR |  | The rate at which the medication was infused. |
| 22 | `MAR_INF_RATE_UNIT_C_NAME` | VARCHAR | org | The unit category number associated with the infusion rate of the administration. |
| 23 | `DOSE_UNIT_C_NAME` | VARCHAR |  | The unit category number associated with the dose of the administration. |
| 24 | `MAR_DURATION` | VARCHAR |  | The length of time the administration took to complete or infuse. |
| 25 | `MAR_DURATION_UNIT_C_NAME` | VARCHAR |  | The duration unit category number associated with the administration. |
| 26 | `DEV_RECV_TIME` | DATETIME (Local) |  | The instant the device recorded this administration data. |
| 27 | `MAR_IMM_LINK_ID` | NUMERIC |  | The unique ID of the immunization associated with this administration. |
| 28 | `OVRD_LINK_STATUS_C_NAME` | VARCHAR |  | The linked override pull status category number of the administration, indicating whether it is linked to a medication order. The status can be 1-"linked", 2-"not linked", or null. |
| 29 | `MAR_OVRD_LNK_USR_ID` | VARCHAR |  | The unique ID of the user that updated the linked status of the override pull administration. |
| 30 | `MAR_OVRD_LNK_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `MAR_ADMIN_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 32 | `MAR_ORD_DAT` | NUMERIC |  | The order contact for this administration. |
| 33 | `SCAN_MODE_YN` | VARCHAR |  | Indicates whether the user scanned at least one barcode for this admin. This column should not be used to report on scanning compliance. |
| 34 | `DUE_ACTION_C_NAME` | VARCHAR |  | The medication administration record (MAR) action that is scheduled when a due time is acted upon. This column will only be populated if Duration-Based Due Actions are configured (LSD 34640 and 34641). |
| 35 | `MAR_BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 36 | `MED_OVRIDE_ALERT_ID` | NUMERIC |  | This column will list the overridden "Med not scanned" alert ID for an administration |
| 37 | `PAT_OVRIDE_ALERT_ID` | NUMERIC |  | This column will list the overridden "Patient not scanned" alert ID for an administration |
| 38 | `MAR_BLOOD_INFO_LN` | INTEGER |  | The line number for the blood unit information associated with this administration. Together with ORDER_MED_ID, this forms the foreign key to the BLOOD_ADMIN_INFO table. |
| 39 | `CYCLIC_RATE_PARENT_LINE` | INTEGER |  | The line number of the parent administration of this cyclic rate change due time. |
| 40 | `MORPHINE_EQUIV_MG_DOSE` | NUMERIC |  | This column stores a non-rate-based or non-continuous medication administration's equivalent dose in terms of milligrams of morphine. This value represents the relative amount of opiates a patient received from the administration. For medications which do not contain an opioid as defined in System Definitions, this value is 0. For continuous opioids and opioids with a rate-based dose, this value is null. Patches are considered to have a rate-based dose for this column. This is not calculated for blood product, feeding product, or patient-controlled analgesic (PCA) administrations. |
| 41 | `MORPHINE_EQUIV_MG_PER_HR_RATE` | NUMERIC |  | This column stores a rate-based or continuous medication administration's equivalent dose rate in terms of milligrams of morphine infused per hour. This value represents the relative amount of opiates a patient received over the duration of the administration. For medications which do not contain an opioid as defined in system definitions, this value will be zero. For non-continuous opioids and opioids with a non-rate-based dose, this value will be null. Patches are considered to have a rated-based dose for this column. This item is not calculated for blood product, feeding product, or patient-controlled analgesic (PCA) administrations. |
| 42 | `ORIGINAL_AMOUNT` | VARCHAR |  | In workflows where weight-based dose simplification or unit conversion can happen, this column contains the originally documented amount. |
| 43 | `ORIGINAL_UNIT_C_NAME` | VARCHAR |  | This column contains the originally documented unit if dose simplification or unit conversion occurred. |
| 44 | `MAR_ORD_CONTACT_DATE_REAL` | FLOAT |  | The ORD contact date for this administration in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 45 | `CUP_IDENT` | VARCHAR |  | This is the ID that dictates which cup an administration belongs to. |
| 46 | `SCHEDULED_DOSE_UNIT_C_NAME` | VARCHAR |  | The scheduled dose unit category ID for the administration. |
| 47 | `SCHEDULED_DOSE` | VARCHAR |  | The dose that was scheduled to be due for the administration of an order with multiple possible doses. |
| 48 | `CONCENTRATION` | VARCHAR |  | The concentration for the administration. |
| 49 | `DUR_BASED_PARENT_LINE` | INTEGER |  | The line number of the administration that created this duration-based due time. |
| 50 | `DUR_BASED_CHILD_LINE` | INTEGER |  | The line number of the duration-based due time administration that was created by this administration. |
| 51 | `CYCLIC_RATE_CHILD_LINE` | INTEGER |  | The line number of the following child administration of this cyclic rate change due time. |
| 52 | `SCHEDULED_AMOUNT` | VARCHAR |  | Scheduled administration amount when the order has multiple doses. |
| 53 | `SCHEDULED_AMOUNT_UNIT_C_NAME` | VARCHAR |  | Scheduled administration amount unit when the order has multiple doses. |
| 54 | `CUP_OVRIDE_ALERT_ID` | NUMERIC |  | This item will list the overridden "Container not scanned" alert for an administration. |
| 55 | `MAR_PEND_USER_ID` | VARCHAR |  | The unique ID of the user with deferred signoff for the administration. |
| 56 | `MAR_PEND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 57 | `MAR_PEND_SECOND_USER_ID` | VARCHAR |  | The verifying user with deferred signoff |
| 58 | `MAR_PEND_SECOND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 59 | `TCI_CONCENTRATION` | VARCHAR |  | Target concentration of the TCI pump |
| 60 | `TCI_CONCENTRATION_UNIT_C_NAME` | VARCHAR |  | Target concentration unit for the TCI pump |
| 61 | `TCI_MODEL_C_NAME` | VARCHAR | org | The model used for the TCI pump |
| 62 | `TCI_TARGET_C_NAME` | VARCHAR | org | The TCI Target category ID for the administration. |
| 63 | `MAR_PSP_IDENT` | VARCHAR |  | This is the identifier that dictates which patient-specific package belongs to an administration. This can also be a comma delimited list of identifiers if multiple patient-specific packages are scanned for a single administration. |
| 64 | `PSP_OVRIDE_ALERT_ID` | NUMERIC |  | This item will list the overridden "Patient-Specific Package not scanned" alert ID for an administration. |
| 65 | `MAR_DUAL_SIGN_SOURCE_C_NAME` | VARCHAR |  | The source of the device the second signer used when approving the administration. For example, whether their signoff took place from a remote location |
| 66 | `PENDED_DUE_ACTION_C_NAME` | VARCHAR |  | The MAR action that should be documented when consuming a due time. |
| 67 | `DUR_BASED_PARENT_ORDER_ID` | NUMERIC |  | For a duration-based child administration, this item stores the order ID of its parent. When the duration-based parent and child administrations are on the same order, this item is null. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

