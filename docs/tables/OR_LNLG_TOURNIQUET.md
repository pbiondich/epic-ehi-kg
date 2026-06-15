# OR_LNLG_TOURNIQUET

> This table contains the tourniquets information for the surgical log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 15  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `TOURN_UNIT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `TOURNIQUET_TYPE_C_NAME` | VARCHAR | org | The type of tourniquet |
| 4 | `TOURNIQUET_AREA_C_NAME` | VARCHAR | org | The body area to which the tourniquet was applied. |
| 5 | `TOURN_AREA_LAT_C_NAME` | VARCHAR | org | The laterality of the body area. |
| 6 | `TOURNIQUET_PRESSUR` | NUMERIC |  | The pressure setting of the tourniquet |
| 7 | `TOURN_CUFF_SIZE_C_NAME` | VARCHAR | org | The tourniquet cuff size category number for the log. |
| 8 | `OCCLUSION_PRESSUR_C_NAME` | VARCHAR | org | The limb occlusion pressure category number indicates if high or low pressure was applied with limb occlusion. |
| 9 | `TOURN_PAD_APPLIED_C_NAME` | VARCHAR |  | Indicates if tourniquet padding was applied. |
| 10 | `TOURN_PULSE_SITE_C_NAME` | VARCHAR | org | Indicates the extremity site where the pre-tourniquet pulse was measured. |
| 11 | `TOURN_PULSE_RYTM_C_NAME` | VARCHAR | org | Indicates the measured pre-tourniquet extremity pulse rhythm. |
| 12 | `TOURNIQUET_PRESSR_2` | NUMERIC |  | This item stores the second tourniquet pressure. |
| 13 | `TOURNIQUET_PRESSR_3` | NUMERIC |  | This item stores the third tourniquet pressure. |
| 14 | `TOURNIQUET_PRESSR_4` | NUMERIC |  | This item stores the fourth tourniquet pressure. |
| 15 | `TOURNIQUET_PRESSR_5` | NUMERIC |  | This item stores the fifth tourniquet pressure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

