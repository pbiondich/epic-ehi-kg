# ORD_RES_BLOOD

> Contains information about a prepared unit of blood. These fields will be populated via an interface.

**Primary key:** `FINDING_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The ID of a finding (RES) that contains the information that matches blood to a certain patient. This record holds information like the unit number, product, expiration, and blood type. |
| 2 | `BLOOD_UNIT_NUMBER` | VARCHAR |  | The primary identifier for the blood product. This is not necessarily unique. Populated via interface for the 'Prepare' order of blood. |
| 3 | `BLOOD_CODING_SYS_C_NAME` | VARCHAR | org | Specifies the coding system used for the Unit Number. |
| 4 | `BLOOD_PRODUCT_CODE` | VARCHAR |  | Secondary identifier to be paired with unit number (when dealing with divisions of a unit of blood). |
| 5 | `BLOOD_CODABAR_REG` | VARCHAR |  | The CODABAR registration number from the bag of blood associated with this record. |
| 6 | `BLOOD_CODABAR_MAP` | VARCHAR |  | Contains the two-digit mapping of the CODABAR registration number that appears in the external unit number. |
| 7 | `BLOOD_EXP_DTTM` | DATETIME (Local) |  | The expiration date for a unit of blood (from the interface). |
| 8 | `BLOOD_UNIT_TYPE` | VARCHAR |  | The blood type (barcode data) of a unit of blood (from the interface). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

