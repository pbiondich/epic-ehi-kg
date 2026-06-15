# HOLOGRAM_SELECTIONS

> This table stores details about each selection made in a hologram record. Which specific details are stored depends on the type of each row.

**Overflow family:** [HOLOGRAM_SELECTIONS_2](HOLOGRAM_SELECTIONS_2.md)  
**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 72  
**Org-specific columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. Note this does not represent an actual date; it simply serves as a unique line identifier in a specific hologram. |
| 3 | `DISPLAY_NAME` | VARCHAR |  | Display name of the selection stored in this contact. |
| 4 | `LEVEL_OF_SERVICE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `SMARTTEXT_TYPE_C_NAME` | VARCHAR | org | The filing type category ID of the SmartText SSI. |
| 6 | `SMARTTEXT_NOTE_TYPE_IP_C_NAME` | VARCHAR | org | The note type category ID potentially filed to if the SmartText type is Inpatient Notes. |
| 7 | `SMARTTEXT_ADDED_NOW_YN` | VARCHAR |  | Indicates whether "Add Now" was used to select the SmartText SSI. "Y" indicates it was; "N" or NULL indicate it was not. |
| 8 | `SMARTTEXT_MAKE_SENSITIVE_YN` | VARCHAR |  | Indicates whether the note this selection will potentially contribute to is marked sensitive. "Y" indicates the note created or added to is marked sensitive. "N" or NULL indicate the sensitivity of the note created or filed to is unaffected by this. |
| 9 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 10 | `DX_DESCRIPTION` | VARCHAR |  | Display name of a diagnosis pended in a HOL record. Dynamic reflection of I SSI 5010. |
| 11 | `DX_QUAL_2_C_NAME` | VARCHAR | org | Qualifier for a diagnosis pended in an HOL record. Dynamic reflection of I SSI 5020. |
| 12 | `DX_COMMENT` | VARCHAR |  | Comment for a diagnosis pended in an HOL record. Dynamic reflection of I SSI 5030. |
| 13 | `DX_PRIMARY_YN` | VARCHAR |  | Whether a diagnosis pended in an HOL record is intended to be marked as the encounter's primary diagnosis. Dynamic reflection of I SSI 5060. |
| 14 | `DX_CHRONIC_YN` | VARCHAR |  | Whether a diagnosis pended in an HOL is a chronic condition. |
| 15 | `IMMUN_ID` | NUMERIC |  | The unique ID of the immunization record associated with this hologram selection. |
| 16 | `IMMUN_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 17 | `IMMNZTN_DOSE` | VARCHAR |  | The dose string, including quantity and unit, for the immunization in this hologram selection. |
| 18 | `IMMNZTN_DOSE_AMOUNT` | NUMERIC |  | The dose quantity for the immunization in this hologram selection. Corresponds to the unit in the IMMNZTN_DISP_QTYUNIT_C column. |
| 19 | `IMMNZTN_DISP_QTYUNIT_C_NAME` | VARCHAR | org | The dose unit category ID for the hologram selection. |
| 20 | `IMMNZTN_ROUTE_C_NAME` | VARCHAR | org | The immunization route category ID for the hologram selection. |
| 21 | `IMMNZTN_SITE_C_NAME` | VARCHAR | org | The immunization site category ID for the hologram selection. |
| 22 | `IMMNZTN_MANUFACTURER_MFG_C_NAME` | VARCHAR | org | The immunization manufacturer category ID for the hologram selection. |
| 23 | `IMMNZTN_LOT_NUMBER` | VARCHAR |  | The lot number for the immunization in this hologram selection. |
| 24 | `IMMNZTN_PRODUCT` | VARCHAR |  | The product for the immunization in this hologram selection. |
| 25 | `IMMNZTN_NDC_ID` | VARCHAR |  | The unique ID of the national drug code associated with the immunization in this hologram selection. |
| 26 | `IMMNZTN_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 27 | `IMMNZTN_IMM_PRODUCT_C_NAME` | VARCHAR | org | The immunization product category ID for the hologram selection. |
| 28 | `IMMNZTN_DATE` | DATETIME |  | The date this immunization was administered. |
| 29 | `IMMNZTN_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The date and time that this immunization was administered. |
| 30 | `IMMNZTN_INVENTORY_CLASS_C_NAME` | VARCHAR |  | The inventory class category ID for the hologram selection. |
| 31 | `IMMNZTN_LOT_NUM_ID_LOT_NUM` | VARCHAR |  | The lot number on the vial for a given medication or immunization. |
| 32 | `IMMNZTN_NEXT_DUE_DATE` | DATETIME |  | Date of the next time this immunization is due. |
| 33 | `IMMNZTN_EXPIRATION_DATE` | DATETIME |  | Expiration date for this immunization. |
| 34 | `IMMNZTN_IMM_DEFER_DUR_C_NAME` | VARCHAR | org | The immunization deferral duration category ID for the hologram selection. |
| 35 | `IMMNZTN_GIVEN_BY_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 36 | `IMMNZTN_GIVEN_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `IMMNZTN_EXTERNAL_ADMIN_C_NAME` | VARCHAR | org | The immunization external administration category ID for the hologram selection. |
| 38 | `IMMNZTN_VIS_DATE` | VARCHAR |  | The issue date of the Vaccine Information Statement provided to the patient for the immunization in this hologram selection. This value is a freetext string, not a discrete date. |
| 39 | `IMMNZTN_DEFER_REASON_C_NAME` | VARCHAR | org | The immunization deferral reason category ID for the hologram selection. |
| 40 | `IMMNZTN_ADMIN_COMMENT` | VARCHAR |  | The immunization administration comment entered by the user who administered the vaccine. |
| 41 | `IMMNZTN_ADMIN_LOCATION` | VARCHAR |  | This item stores the physical location where the immunization was administered. Note this column does not network to a location table. |
| 42 | `IMMNZTN_STATUS_C_NAME` | VARCHAR |  | The immunization status category ID for the hologram selection. |
| 43 | `LOS_COMPONENT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 44 | `COMPONENT_LOS_NEW_OR_EST_C_NAME` | VARCHAR |  | The new or established patient category ID for the level of service component. |
| 45 | `LOS_COMPONENT_COUNSEL_TIME` | INTEGER |  | Level of service component counseling time. |
| 46 | `COMPONENT_LOS_HX_LEVEL_C_NAME` | VARCHAR |  | The history level category ID for the level of service component. |
| 47 | `COMPONENT_LOS_EXAM_LEVEL_C_NAME` | VARCHAR |  | The exam level category ID for the level of service component. |
| 48 | `COMPONENT_LOS_MDM_LEVEL_C_NAME` | VARCHAR |  | The MDM level category ID for the level of service component. |
| 49 | `LOS_COMPONENT_PROC_CALC_YN` | VARCHAR |  | Indicates whether the level of service component procedure ID was calculated ('Y') or not calculated ('N' or NULL). |
| 50 | `FUP_NUMBER_OF_UNITS` | INTEGER |  | Follow-up number of units. |
| 51 | `FUP_TYPE_OF_UNIT_C_NAME` | VARCHAR |  | Category from I EPT 18314. |
| 52 | `FUP_APPROX_YN` | VARCHAR |  | Follow-up approximately checkbox value. Category from ECT 100. |
| 53 | `FUP_PRN_YN` | VARCHAR |  | Follow-up PRN checkbox value. Category from ECT 100. |
| 54 | `FUP_RETURN_FOR_TEXT` | VARCHAR |  | Free-text note indicating what the follow-up is for. |
| 55 | `FUP_CODIFIED_C_NAME` | VARCHAR | org | Category from I EPT 18210, but stored in I EPT 18330. Used to store the method of follow-up. |
| 56 | `FUP_INSTRUCTIONS_CODIFIED_C_NAME` | VARCHAR | org | Category from I EPT 18211, but stored in I EPT 18331. Used to store special instructions for the follow-up. |
| 57 | `FUP_COPY_TO_PCP_YN` | VARCHAR |  | Category value from ECT 100 to indicate if the patient's primary care provider should automatically be included as a recipient when documenting the follow-up. |
| 58 | `FUP_SEND_REMINDER_YN` | VARCHAR |  | Category from ECT 100. Used to determine if a reminder should be sent for the follow-up. |
| 59 | `FUP_REMINDER_DAYS` | INTEGER |  | The number of days to wait until the follow-up reminder message is sent. |
| 60 | `FUP_PRN_TEXT` | VARCHAR |  | Text explaining when the patient should follow up PRN. |
| 61 | `FUP_REMINDER_MESSAGE` | VARCHAR |  | Message that will be sent as a follow-up reminder. |
| 62 | `FUP_ROUTING_PRIORITY_C_NAME` | VARCHAR | org | Follow-up chart routing priority. |
| 63 | `FUP_ROUTING_COMMENT` | VARCHAR |  | Follow-up chart routing comments. |
| 64 | `FUP_USER_ACCEPTED_YN` | VARCHAR |  | Category from ECT 101 to track whether the user has accepted the follow-up details. |
| 65 | `NT_DISPOSITION_PHONE_DISP_C_NAME` | VARCHAR | org | Disposition from category EPT 17400. |
| 66 | `NT_DISPOSITION_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 67 | `NT_DISPOSITION_COMMENT` | VARCHAR |  | Disposition comment. |
| 68 | `NT_DISPOSITION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 69 | `NT_DISP_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The disposition instant stored in UTC format. |
| 70 | `REASON_FOR_VISIT_RFV_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |
| 71 | `REASON_FOR_VISIT_COMMENT` | VARCHAR |  | Contains free text comments about a reason for visit that is being temporarily stored in a hologram record. Dynamic reflection of I SSI 10010. |
| 72 | `REASON_FOR_VISIT_ONSET_DATE` | DATETIME |  | Contains onset date for a reason for visit that is being temporarily stored in a hologram record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

