# OR_LNLG_ESU

> This table contains Electro Surgery Units information for the surgical log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 36  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ELECT_SURG_DEV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `ELCT_SRG_MOD_TYP_C_NAME` | VARCHAR | org | The ESU device mode type. |
| 4 | `ELECT_SURG_LOC_C_NAME` | VARCHAR | org | The location at which the ESU was applied. |
| 5 | `ELECT_SURG_LATER_C_NAME` | VARCHAR | org | The laterality of the location. |
| 6 | `ESD_TYPE_C_NAME` | VARCHAR | org | The ESU device type. |
| 7 | `ELECT_SURG_COAG_SE` | NUMERIC |  | The ESU coagulation settings. |
| 8 | `ELECT_SURG_CUT_SET` | NUMERIC |  | The ESU cut settings. |
| 9 | `ELECT_SURG_BSET_C_NAME` | VARCHAR | org | Stores the blend settings for the Electro Surgery Device. |
| 10 | `ELECT_SURG_COAG_HGH` | NUMERIC |  | Documents the high coagulation setting of a particular electrosurgical device. |
| 11 | `ELECT_SURG_CUT_HIGH` | NUMERIC |  | Documents the high cut setting of a particular electrosurgical device. |
| 12 | `ELECT_SURG_GPAPP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `ELECT_SURG_PAD_LOT` | VARCHAR |  | Documents the lot number of the ESU's grounding pad. |
| 14 | `GROUND_PAD_EXP_DT` | DATETIME |  | This item stores the expiration date for an ESU grounding pad. |
| 15 | `BIPOLAR_SETTING` | NUMERIC |  | This item stores the bipolar setting for an Electro Surgery Device. This is the voltage. |
| 16 | `MONO_CUT_SETTING_C_NAME` | VARCHAR | org | The monopolar cut setting category number for the electro surgery unit. |
| 17 | `MONO_COAG_SETTING_C_NAME` | VARCHAR | org | The monopolar coagulation setting category number for the electro surgery unit. |
| 18 | `ESU_COAG_WATTAGE` | INTEGER |  | Stores information about the wattage for the coagulation setting of the electro surgery unit. |
| 19 | `ESU_CUT_WATTAGE` | INTEGER |  | Stores information about the wattage for the cut setting of the electro surgery unit. |
| 20 | `ESU_BIPOLAR_WATTAG` | INTEGER |  | Stores information about the wattage for the bipolar setting of the electro surgery unit. |
| 21 | `LIGASURE_ONE_LOW_C_NAME` | VARCHAR | org | The category number for the Ligasure 1 Low item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 22 | `LIGASURE_ONE_HIGH_C_NAME` | VARCHAR | org | The category number for the Ligasure 1 High item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 23 | `LIGASURE_TWO_LOW_C_NAME` | VARCHAR | org | The category number for the Ligasure 2 Low item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 24 | `LIGASURE_TWO_HIGH_C_NAME` | VARCHAR | org | The category number for the Ligasure 2 High item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 25 | `BIPOLAR_COAG_LOW` | INTEGER |  | The low bipolar coagulation setting for the electro surgery unit. |
| 26 | `BIPOLAR_COAG_HIGH` | INTEGER |  | The high bipolar coagulation setting for the electro surgery unit (ESU). |
| 27 | `BIPOLAR_SETTINGS_C_NAME` | VARCHAR | org | The category number for the Bipolar Output Settings item. |
| 28 | `GROUND_PAD_SER_NUM` | VARCHAR |  | This item stores the serial number of the ESU grounding pad. |
| 29 | `ELECT_SURG_PRESET_C_NAME` | VARCHAR | org | Store settings for ESU device. |
| 30 | `ESU_GAS_FLOW_HIGH` | NUMERIC |  | The high gas flow rate for the electro surgery unit. |
| 31 | `ESU_GAS_FLOW_LOW` | NUMERIC |  | The low gas flow rate for the electro surgery unit. |
| 32 | `ESU_COAG_SETTING` | NUMERIC |  | Item to document medium setting of ESU machines. |
| 33 | `ESU_CUT_SETTING` | NUMERIC |  | Item to document medium cut setting of ESU machines. |
| 34 | `ESU_MODULATION` | INTEGER |  | This item stores the numerical modulation setting for Electro Surgical Equipment. |
| 35 | `ESU_BIPOLAR_CUT_LOW` | NUMERIC |  | Documents the low cut setting of a bipolar electrosurgical device. |
| 36 | `ESU_BIPOLAR_CUT_HI` | NUMERIC |  | Documents the high cut setting of a bipolar electrosurgical device. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

