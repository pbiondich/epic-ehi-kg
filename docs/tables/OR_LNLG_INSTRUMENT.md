# OR_LNLG_INSTRUMENT

> This table contains the Instruments information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 22  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `INSTRUMENT_TYPE_C_NAME` | VARCHAR | org | The instrument type. |
| 3 | `INSTRUMENT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `INSTRUMENT_FLASH_YN` | VARCHAR |  | This item stores whether or not an instrument has been flash-sterilized. |
| 5 | `FLSH_AUTCLVE_C_NAME` | VARCHAR | org | The autoclave category number that was used to sterilize this instrument. |
| 6 | `FLSH_LOAD` | VARCHAR |  | The load batch ID that this instrument was flash sterilized in. |
| 7 | `FLSH_RSN_C_NAME` | VARCHAR | org | The category number of the reason that this instrument was flash sterilized. |
| 8 | `FLSH_VER_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `FLSH_RSLT_C_NAME` | VARCHAR | org | The category number of the result of this instruments flash sterilization process. |
| 10 | `FLSH_PRE_RSN_C_NAME` | VARCHAR | org | The category number of the reason this instrument was pre-released in the flash sterilization process. |
| 11 | `FLSH_CYCLE_TYPE_C_NAME` | VARCHAR | org | The category number of the cycle type of the flash autoclave. |
| 12 | `FLSH_AUTCLVE_TEMP` | NUMERIC |  | The category number of the temperature of the flash autoclave. |
| 13 | `FLSH_AUTCLVE_PRES` | NUMERIC |  | The category number of the pressure of the flash autoclave. |
| 14 | `FLSH_PRES_UNIT_C_NAME` | VARCHAR |  | The category number of the unit of pressure of the flash autoclave. |
| 15 | `FLSH_DURATION` | VARCHAR |  | The duration of time (in minutes) an item was flash sterilized. |
| 16 | `FLSH_DATE` | DATETIME |  | This item stores the date an instrument was sterilized. |
| 17 | `FLSH_TIME` | DATETIME (Attached) |  | This item stores the time an instrument was sterilized. |
| 18 | `FLSH_BIOL_RSLT_TIME` | DATETIME (Attached) |  | This item stores the time a biological growth test was performed for sterile implants. |
| 19 | `INSTR_BARCODE_ID` | VARCHAR |  | This item is used to document an instrument's barcode ID. |
| 20 | `FLSH_BIOL_RSLT_USER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 21 | `STERILIZATION_REFERENCE_NUM` | INTEGER |  | The sterilization reference number. |
| 22 | `STERILIZATION_EXP_DATE` | DATETIME |  | This item is used to store the sterilization expiration date of the equipment or instrument. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

