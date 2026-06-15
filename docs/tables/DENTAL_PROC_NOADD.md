# DENTAL_PROC_NOADD

> This table contains the items for dental procedure records.

**Primary key:** `FINDING_ID`  
**Columns:** 32  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `DENTAL_EAP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `DENTAL_COMP_INST_DTTM` | DATETIME (Attached) |  | Date and time dental procedure was completed |
| 4 | `DENTAL_PROC_STAT_C_NAME` | VARCHAR |  | Current status of the dental procedure |
| 5 | `DENTAL_PROC_ARCH_C_NAME` | VARCHAR |  | Identifies which arch the dental procedure is for. |
| 6 | `DENTAL_QUADRANT_C_NAME` | VARCHAR |  | Identifies which quadrant the dental procedure is for. |
| 7 | `DENTAL_PROC_VISIT_ID` | NUMERIC |  | Identifies the visit in which a dental procedure is planned to be completed. |
| 8 | `DENTAL_COMP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `DEN_PROC_EX_FLAG_YN` | VARCHAR |  | Indicates whether a procedure existed as part of the patient's presenting condition. |
| 10 | `DENTAL_TOOTH_AREA_C_NAME` | VARCHAR |  | This determines the part of the tooth that a procedure or finding affects. |
| 11 | `DENT_PLAN_VISIT_NUM` | INTEGER |  | Identifies the visit number that a procedure is being planned for. |
| 12 | `DENTAL_BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `DENT_PLAN_PRL_ID` | NUMERIC |  | Stores the treatment template that will be used when the user creates a treatment plan for the dental procedure |
| 14 | `DENT_PLAN_PRL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 15 | `DENT_PROC_BY_RULE_YN` | VARCHAR |  | Indicates whether a procedure is added by auto-treatment planning rule. |
| 16 | `DENTAL_PROC_IMP_ID` | VARCHAR |  | Stores implant record ID linked to a dental procedure. |
| 17 | `DENTAL_PROSTH_ID` | VARCHAR |  | Stores the unique identifier for a multi-tooth prosthetic structure. This is only used in Finland. |
| 18 | `DENTAL_PROC_AREA_C_NAME` | VARCHAR |  | Specifies the area of the oral cavity that a dental procedure is performed on. |
| 19 | `DENTAL_LNKED_ORD_ID` | NUMERIC |  | This column contains the linked order record for a dental procedure. |
| 20 | `DENTAL_PROC_NOTE_ID` | VARCHAR |  | ID of the note (HNO) record that serves as this dental procedure's Completion Details note |
| 21 | `DENTAL_TRIG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 22 | `DENT_PROC_SUBSTATUS_C_NAME` | VARCHAR | org | Subcategorization of a dental procedure |
| 23 | `DENTAL_LINKED_BRIDGE_PROC` | NUMERIC |  | The procedure (RES) ID that indicates which bridge this dental procedure forms a part of. All of the procedures that are in the same bridge have the same value for this column. |
| 24 | `DEN_SRC_PROTOCOL_ID` | NUMERIC |  | The SmartSet this result came from |
| 25 | `DEN_SRC_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 26 | `D_SS_PRL_SRC_TYPE_C_NAME` | VARCHAR |  | Result came from PRL OrderSet, PRL SmartSet, or PRL Template |
| 27 | `DENT_SRC_PRL_DAT` | VARCHAR |  | The DAT of the SmartSet as applied to the patient |
| 28 | `DENT_PROC_AREA_INACTIVE_YN` | VARCHAR |  | Determines if a non-tooth level procedure should be considered active and displayed on tooth chart |
| 29 | `DENT_PRL_INST_DTTM` | DATETIME (Local) |  | The Instant the Procedure was created from a PRL template |
| 30 | `DENT_PROC_DNF_ID` | NUMERIC |  | The linked procedure (RES) ID that was marked Did Not Finish, to be completed in a subsequent visit |
| 31 | `DENT_REPL_PROSTH_YN` | VARCHAR |  | Whether or not the dental procedure is a replacement prosthesis. |
| 32 | `DENT_REPL_PROSTH_DATE` | DATETIME |  | The date of prior placement of a prosthesis procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

