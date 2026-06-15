# OR_LNLG_OTH_EQUIP

> This table contains the Other Equipment information for the procedural log.

**Primary key:** `RECORD_ID`  
**Columns:** 38  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `OTHER_EQUIP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `OTHER_EQUIP_SET_T_NAME` | VARCHAR | org | The setting type for the other equipment. |
| 4 | `OTHER_EQUIP_SET_HI` | NUMERIC |  | The high setting for the equipment. |
| 5 | `OTHER_EQUIP_SET_LO` | NUMERIC |  | The low setting for the equipment |
| 6 | `OTH_EQUIP_TYPE_C_NAME` | VARCHAR | org | The type of the other equipment. |
| 7 | `HYST_PUMP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `HYST_PUMP_PRESSURE` | NUMERIC |  | The pressure setting (mmHg) for the hysteroscopy pump. |
| 9 | `HYST_PUMP_DEFICIT` | NUMERIC |  | The deficit setting (mL) for the hysteroscopy pump. |
| 10 | `HYST_PUMP_T_INFLOW` | NUMERIC |  | The total inflow setting (mL) for the hysteroscopy pump. |
| 11 | `LAP_SCN_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `CELL_SAVER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `CELL_SAVER_NUM` | VARCHAR |  | The numeric or alphanumeric identifier for the cell saver machine. |
| 14 | `HYST_PUMP_ALM_SE_YN` | VARCHAR |  | Indicates whether the hysteroscopy pump alarm settings are within limits. Y indicates that the alarm settings are within limits. N indicates that the alarm settings are not within limits. |
| 15 | `LAP_SCN_PRERD_C_NAME` | VARCHAR | org | The category title of the pre-op reading (intact/compromised/NA) for the laparoscopic instrument scan. |
| 16 | `LAP_SCN_POSTRD_C_NAME` | VARCHAR |  | The category title of the post-op reading (intact/compromised/NA) for the laparoscopic instrument scan. |
| 17 | `OTHER_EQUIP_LAT_C_NAME` | VARCHAR | org | This item stores laterality for other equipment. |
| 18 | `OTHER_EQUIP_CAV_WID` | NUMERIC |  | Document the cavity width measurement, as measured by other equipment type. |
| 19 | `OTHER_EQUIP_CAV_LEN` | NUMERIC |  | Document the cavity length measurement, as measured by other equipment type. |
| 20 | `OTHER_EQUIP_PWR_LOW` | INTEGER |  | Document the low power for other equipment type. |
| 21 | `OTHER_EQUIP_PWR_HI` | INTEGER |  | Document the high power for other equipment type. |
| 22 | `OTH_EQUIP_PWR_UNI_C_NAME` | VARCHAR | org | Document the power unit for other equipment type. |
| 23 | `HYST_PUMP_T_OUTFLOW` | NUMERIC |  | The total outflow setting (mL) for the hysteroscopy pump. |
| 24 | `CELL_SVR_VOL_PROC` | INTEGER |  | This column contains information about the number of milliliters of blood processed during surgery. |
| 25 | `CELL_SVR_VOL_REINFU` | INTEGER |  | This column contains information about the number of milliliters of blood reinfused during surgery. |
| 26 | `NUMBER_OF_CYCLES` | INTEGER |  | This item stores the number of cycles setting for a piece of ablation equipment. |
| 27 | `NUMBER_OF_SITES` | INTEGER |  | This item stores the number of ablation sites to which this piece of equipment was applied. |
| 28 | `TEMPERATURE` | NUMERIC |  | This item stores the temperature for a piece of ablation equipment. |
| 29 | `OTHER_EQUIP_VOLUME` | NUMERIC |  | This item stores the volume, as measured by other equipment type. |
| 30 | `OTHER_EQUIP_SER_NUM` | NUMERIC |  | This item stores the serial number of other equipment type. |
| 31 | `AVERAGE_POWER` | NUMERIC |  | The average power used. |
| 32 | `OTHER_EQUIP_SOUNDING_LEN` | NUMERIC |  | This column stores the sounding length measurement in centimeters, as measured by a piece of equipment. |
| 33 | `OTHER_EQUIP_SETTING_ADDITIONAL` | NUMERIC |  | This column stores additional equipment settings. |
| 34 | `CELL_SVR_VOL_NOT_PROCESSED` | INTEGER |  | The milliliters of blood not processed. |
| 35 | `CELL_SVR_VOL_WASTED` | INTEGER |  | The milliliters of blood wasted. |
| 36 | `CELL_SVR_IRRIGATION_VOL` | NUMERIC |  | This column stores the Irrigation volume used for cell saver. |
| 37 | `CELL_SVR_ANTICOAG_VOL` | NUMERIC |  | This column stores the anti-coagulant volume used for cell saver. |
| 38 | `IMPLANT_ON_CART_YN` | VARCHAR |  | If there was an implant not on the cart. Used for comprehensive steam sterilization (IUSS) documentation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

