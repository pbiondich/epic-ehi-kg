# OR_LNLG_ROBOTICS

> This table contains the Robotics information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUB_PROC_NAME_C_NAME` | VARCHAR | org | The name of the subprocedure of the robotics procedure. The specific items are extracted in table ZC_SUB_PROC_NAME. |
| 4 | `SUB_PROC_PT_POS_C_NAME` | VARCHAR | org | The position of the patient during the subprocedure of the robotics procedure. The specific items are extracted in table ZC_SUB_PROC_PT_POS. |
| 5 | `PORT_PL_DATE` | DATETIME (Local) |  | The date and time at which the port was placed during the subprocedure of the robotics procedure. |
| 6 | `DOCK_START_DATE` | DATETIME (Local) |  | The date and time at which the robot was docked during the subprocedure of the robotics procedure. |
| 7 | `CONSOLE_START_DATE` | DATETIME (Local) |  | The date and time at which the console was started for the subprocedure of the robotics procedure. |
| 8 | `CONSOLE_END_DATE` | DATETIME (Local) |  | The date and time at which the console was stopped during the subprocedure of the robotics procedure. |
| 9 | `DOCK_END_DATE` | DATETIME (Local) |  | The date and time at which the robot was undocked during the subprocedure of the robotics procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

