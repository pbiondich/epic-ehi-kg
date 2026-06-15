# TX_ANES_INFO

> The TX_ANES_INFO table contains one record for each anesthesia transaction record in your system. The data contained in each record consists of no-add, single-response anesthesia information.

**Primary key:** `TX_ID`  
**Columns:** 22  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given transaction. |
| 2 | `SUP_UNIT_PX_TOT` | NUMERIC |  | The total number of units of supplemental unit procedures for this procedure. |
| 3 | `AGE_UNIT_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `EMERG_UNIT_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `IS_INDPNDT_CRNA_YN` | VARCHAR |  | Indicates whether this is an independent Certified Registered Nurse Anesthetist (CRNA) charge transaction. Y indicates it is an independent CRNA charge, and N or null indicate it is not an independent CRNA charge. |
| 6 | `ASA_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `AGE_UNT_PX_UNIT` | NUMERIC |  | If your Anesthesia Pricing master file is set up to use age and emergency unit procedures, this column holds the value of the number of anesthesia age unit procedure units for this charge. |
| 8 | `EMERG_UNIT_PX_UNIT` | NUMERIC |  | If your Anesthesia Pricing master file is set up to use age and emergency unit procedures, this column holds the value of the number of anesthesia emergency unit procedure units for this charge. |
| 9 | `SUP_PX_TYPE_C_NAME` | VARCHAR |  | If your Anesthesia Pricing master file is set up to use age and emergency unit procedures, this column specifies the special procedure type: 1) Age Unit 2) Emergency Unit |
| 10 | `ANESTHESIA_TYPE_C_NAME` | VARCHAR | org | The anesthesia type category number for the anesthesia charge. |
| 11 | `EMERGENCY_STATUS_YN` | VARCHAR |  | Indicates whether the anesthesia charge has an emergency status. |
| 12 | `PHYSICAL_STATUS_C_NAME` | VARCHAR | org | The physical status category number for the anesthesia charge. |
| 13 | `CONCURRENCY_OVERRID` | NUMERIC |  | The concurrency value that overrode the standard concurrency value that was calculated. |
| 14 | `BASE_UNITS` | NUMERIC |  | The uniform factor applied for this anesthesia transaction regardless of the procedure’s length. |
| 15 | `TIMED_UNITS` | NUMERIC |  | The time units for this anesthesia transaction as determined by the length of the procedure. |
| 16 | `PHYSICAL_ST_UNITS` | NUMERIC |  | The physical status units for this anesthesia transaction. |
| 17 | `EMERGENCY_UNITS` | NUMERIC |  | The emergency units for this anesthesia transaction. |
| 18 | `AGE_UNITS` | NUMERIC |  | The age units for this anesthesia transaction. |
| 19 | `CRNA_CHARGE_ID` | NUMERIC |  | The unique ID of the certified registered nurse anesthetist (CRNA) charge transaction that is associated with this anesthesia transaction. |
| 20 | `ORIG_ANES_CHG_ID` | NUMERIC |  | The unique ID of the anesthesia charge transaction that is associated with this certified registered nurse anesthetist (CRNA) transaction. |
| 21 | `MED_SUP_MOD_OVR_YN` | VARCHAR |  | Indicates whether or not the modifier based on the concurrency calculation for this anesthesia transaction that is normally included on claims has been overridden with the modifier corresponding to a medically supervised case. |
| 22 | `BASE_UNIT_OVERRIDE` | INTEGER |  | This specifies that the base unit has been overridden. The previous base units are stored in it, if this is empty then the base units are not overridden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

