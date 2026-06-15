# ARPB_TX_DENTAL

> This table is used for dental related transaction information.

**Primary key:** `TX_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number category ID for the charge. |
| 3 | `ARCH_C_NAME` | VARCHAR |  | Displays the dental arch used for the procedure. The value displayed will be either Upper or Lower. |
| 4 | `QUADRANT_C_NAME` | VARCHAR |  | Displays the dental quadrant used for the procedure. The value displayed could be one of several options, such as Lower Left or Maxillary Area. |
| 5 | `AREA` | VARCHAR |  | Displays the dental area used for the procedure. The displayed value will be a range of teeth. For example 1-2,10-B, or A-B. |
| 6 | `SUPERNUMERARY_YN` | VARCHAR |  | Indicates whether multiple teeth are present in the socket. |
| 7 | `FOLLOW_UP_MONTHS` | INTEGER |  | The number of months after which this procedure requires follow-up. |
| 8 | `HYGIENIST_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `TREATMENT_PLAN_ID` | VARCHAR | shared | The unique ID of the treatment plan used in this procedure. |
| 10 | `FOLLOW_UP_DATE` | DATETIME |  | Displays the date the recall must be made by. |
| 11 | `DENTAL_CHG_TYPE_C_NAME` | VARCHAR |  | Indicates what type of orthodontic or predetermination charge it is. |
| 12 | `DENTAL_PREAUTH_AMT` | NUMERIC |  | The amount that gets set on predetermination claims for the predetermination dental charge. |
| 13 | `DENTAL_PREAUTH_QTY` | INTEGER |  | The quantity that gets set on predetermination claims for the predetermination dental charge. |
| 14 | `CHARGING_PLAN_LINE` | INTEGER |  | The line of the dental charging plan that led to the charge being dropped. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

