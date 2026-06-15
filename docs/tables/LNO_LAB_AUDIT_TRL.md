# LNO_LAB_AUDIT_TRL

> This table contains information for the audit trail of Patient Summary Extract (LNO) records.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the LNO record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRINT_INSTANT` | DATETIME (Local) |  | These are the instants that copies of the report were printed. |
| 4 | `DEVICE_ID` | NUMERIC | FK→ | These are the devices used to print the report. |
| 5 | `DEVICE_ID_PRINT_DEVICE_NAME` | VARCHAR |  | The printer name. |
| 6 | `FREE_TEXT_FAX_NUM` | VARCHAR |  | These are the numbers of the fax machines the report was sent to. |
| 7 | `NUM_OF_COPIES` | INTEGER |  | These are the number of copies of the report sent to each given destination. |
| 8 | `REQUESTING_USER_ID` | VARCHAR |  | These are the users who requested a copy of the report. |
| 9 | `REQUESTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `RCPNT_EMPLOYEE_ID` | VARCHAR |  | These are the employees who received a copy of the report. |
| 11 | `RCPNT_EMPLOYEE_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `RCPNT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `RCPNT_FREE_TEXT` | VARCHAR |  | These are the recipients of the report in freetext. |
| 14 | `RCPNT_SUBMITTER_ID` | NUMERIC |  | These are the submitters which received a copy of the report. |
| 15 | `RCPNT_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 16 | `TYPE_OF_RECIP_C_NAME` | VARCHAR |  | For each provider recipient of the report, this indicates if the provider is an authorizing provider, a PCP, or a CC recipient. |
| 17 | `RCPNT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 18 | `RCPNT_PT_RQG_ID` | NUMERIC |  | Stores the patient who received a copy of the report. The patient database is RQG. |
| 19 | `ADDRESS_SOURCE_C_NAME` | VARCHAR |  | The source which was used to select the destination address for the recipient report. |
| 20 | `DEVICE_SOURCE_C_NAME` | VARCHAR |  | The source which was used to select the printing/faxing device for the recipient report. |
| 21 | `ADDRESS_IDENT` | VARCHAR |  | The unique address identifier which was used to select the destination address for the recipient report. The selected address may differ from the preferred address when a fax is desired and the preferred address does not include a fax. This is currently used for storing provider address unique identifier (SER-21000) when they are used for result report generation. |
| 22 | `PREFERRED_ADDRESS_IDENT` | VARCHAR |  | The unique address identifier which was preferred to be used to select the destination address for the recipient report. The selected address may differ from the preferred address when a fax is desired and the preferred address does not include a fax. This is currently used for storing provider address unique identifier (SER-21000) when they are used for result report generation. |
| 23 | `PREFERRED_ADDRESS_SOURCE_C_NAME` | VARCHAR |  | The source which was used to select the preferred address for the recipient report. The selected address source may differ from the preferred address source when a fax is desired and the preferred address does not include a fax. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DEVICE_ID` | [DEVICE_INFO](DEVICE_INFO.md) | sole_pk | high |

