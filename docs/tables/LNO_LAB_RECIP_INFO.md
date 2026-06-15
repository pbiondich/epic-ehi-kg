# LNO_LAB_RECIP_INFO

> Recipient information for lab result report (LNO) records.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 48  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the LNO record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RCPNT_ORDER_ID` | NUMERIC |  | Stores the order record for which a report will be printed or has printed for the given recipient. |
| 4 | `RECIPIENT_TYPE_C_NAME` | VARCHAR |  | Stores the report's recipient type. |
| 5 | `RECIPIENT_STATUS_C_NAME` | VARCHAR |  | Stores the status of the report which will be printed or has printed for the given recipient. |
| 6 | `RECIPIENT_EVNT_INST` | DATETIME (Local) |  | Stores the instant this line was added to the recipient's table. |
| 7 | `RCPT_RRT_SUB_TYPE_C_NAME` | VARCHAR |  | Stores the sub type of the report. |
| 8 | `RCPNT_TYPE_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `RCPNT_TYPE_SMT_ID` | NUMERIC |  | Stores the submitter record if the recipient is the submitter. |
| 10 | `RCPNT_TYPE_SMT_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 11 | `RCPNT_TYPE_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `RCPNT_TYPE_RQG_ID` | NUMERIC |  | Stores the patient/source record if the recipient is a non enterprise patient. |
| 13 | `RCPNT_TYPE_EMP_ID` | VARCHAR |  | Stores the employee record if the recipient is the employee. |
| 14 | `RCPNT_TYPE_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `RCPNT_TYPE_FREE_TXT` | VARCHAR |  | Stores the free text name of the recipient. |
| 16 | `RCPNT_HOLD_TYPE_C_NAME` | VARCHAR |  | The recipient hold type category number for the recipient. |
| 17 | `RCPNT_HOLD_OVT_LN` | INTEGER |  | Contains the recipient hold test (OVT) line. |
| 18 | `RCPNT_HOLD_BSDON_C_NAME` | VARCHAR |  | Contains the recipient hold based on address category. |
| 19 | `RCPNT_HOLD_QUAL_LN` | INTEGER |  | Contains the recipient hold rule qualifier line. |
| 20 | `RCPNT_RSLN_C_NAME` | VARCHAR | org | The recipient hold resolution category number for the recipient. |
| 21 | `RCPNT_RSLN_INST` | DATETIME (Local) |  | Contains the recipient hold resolution instant. |
| 22 | `RCPNT_RSLN_USER_ID` | VARCHAR |  | Contains the recipient hold resolution user. |
| 23 | `RCPNT_RSLN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `RCPNT_RSLN_LINE` | INTEGER |  | Contains the line in the related group for the recipient hold resolution instant that audits the chosen CC recipient |
| 25 | `RCPNT_LPP_ID` | NUMERIC |  | Stores the programming point which added this recipient |
| 26 | `RCPNT_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 27 | `RCPNT_RPTBL_RULE_YN` | VARCHAR |  | Indicates if the recipient on the row was added because of a reportable rule. |
| 28 | `RCPNT_CORRECTED_RPT` | INTEGER |  | If the report on the row was sent to a health agency based on a reportable rule, and the results later change such that it is no longer reportable to the health agency, this item stores the row in the LNO_LAB_RECIP_INFO table that contains the corrected report. |
| 29 | `RESEND_EMP_ID` | VARCHAR |  | The ID of the user who resent the message. Messages sent over an interface may sometimes fail to deliver and would need to be resent. This column will have a value only for resent messages. |
| 30 | `RESEND_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `RESEND_RELATED_LN` | INTEGER |  | The line number of the associated recipient's record. This points to the recipient line of the interface message that was resent. Messages sent over an interface may sometimes fail to deliver and would need to be resent. This column will have a value only for resent messages. |
| 32 | `RESEND_REASON_C_NAME` | VARCHAR | org | The category number of the reason for resending an interface message. Messages sent over an interface may sometimes fail to deliver and would need to be resent. This column will have a value only for resent messages. |
| 33 | `RESULT_TRGR_LPP_ID` | NUMERIC |  | The ID of the extension that triggered the result. This column will have a value only for those results that were triggered by a post event extension set up to send results over an interface. |
| 34 | `RESULT_TRGR_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 35 | `WHO_REMOV_RECPNT_ID` | VARCHAR |  | The user ID of the user who removed this recipient from result reports. |
| 36 | `WHO_REMOV_RECPNT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `RECPNT_REMOV_RSN_C_NAME` | VARCHAR | org | The category number of the reason for which this recipient was removed from result reports. |
| 38 | `RCPNT_OVRD_DEV_ID` | NUMERIC |  | The record ID of the override device that the recipient is to use when the report prints. |
| 39 | `RCPNT_OVRD_DEV_ID_PRINT_DEVICE_NAME` | VARCHAR |  | The printer name. |
| 40 | `RCPNT_OVRD_FAX_NUM` | VARCHAR |  | The override fax number that the recipient is to use when the report prints. |
| 41 | `RCPNT_RPTBL_RULE_ID` | NUMERIC |  | This item stores the record ID for the reporting rule that caused the recipient to be added. |
| 42 | `RCPNT_RPTBL_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the reporting rule. |
| 43 | `RCPNT_OVRD_ADDRESS_SOURCE_C_NAME` | VARCHAR |  | The source which was used to select the destination override address for the recipient report. |
| 44 | `RCPNT_OVRD_DEVICE_SOURCE_C_NAME` | VARCHAR |  | The source which was used to select the override printing/faxing device for the recipient report. |
| 45 | `RECIP_SUSC_PREF_LINE` | INTEGER |  | Stores the line in related group LNO 51266 that holds which susceptibility tests in the order were reported to the submitter recipient. |
| 46 | `RCP_OVERRIDE_ADDRESS_IDENT` | VARCHAR |  | The unique address identifier which was used to select the destination override address for the recipient report. The selected address may differ from the preferred address when a fax is desired and the preferred address does not include a fax. This is currently used for storing provider address unique identifier (SER-21000) when they are used for result report generation. |
| 47 | `RCP_OVR_PREF_ADDRESS_IDENT` | VARCHAR |  | The unique address identifier which was preferred to be used to select the destination override address for the recipient report. The selected address may differ from the preferred address when a fax is desired and the preferred address does not include a fax. This is currently used for storing provider address unique identifier (SER-21000) when they are used for result report generation. |
| 48 | `RCP_OVRD_PREF_ADDRESS_SOURCE_C_NAME` | VARCHAR |  | The source which was preferred to be used to select the destination override address for the recipient report. The selected address source may differ from the preferred address source when a fax is desired and the preferred address does not include a fax. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

