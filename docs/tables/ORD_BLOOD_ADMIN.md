# ORD_BLOOD_ADMIN

> Administrable Procedure Items in Orders (ORD).

**Primary key:** `ORDER_ID`  
**Columns:** 20  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the child/instance order that is associated with transfusion documentation for a unit of blood. |
| 2 | `ADMIN_PX_TYPE_C_NAME` | VARCHAR |  | Type for procedure that can be administered. |
| 3 | `BLOOD_UNIT_NUM` | VARCHAR |  | The primary identifier for the blood product. This is not necessarily unique. Populated via interface, or administration form for procedures. |
| 4 | `BLOOD_CODING_SYS_C_NAME` | VARCHAR | org | Specifies the coding system used for the Unit Number. Some examples are ISBT 128 and Codabar. |
| 5 | `BLOOD_UNIT_NM_SRC_C_NAME` | VARCHAR |  | Indicates if populated through interface or by user. |
| 6 | `BLOOD_PRODUCT_CODE` | VARCHAR |  | Secondary identifier to be paired with unit number (when dealing with divisions of a unit of blood). |
| 7 | `BLOOD_EXPIRATN_INST` | DATETIME (Local) |  | The expiration instant as specified on the unit of blood. This may be populated by the interface. |
| 8 | `BLOOD_START_INSTANT` | DATETIME (Local) |  | Based on administration actions, the start of the transfusion. |
| 9 | `BLOOD_END_INSTANT` | DATETIME (Local) |  | Based on administration actions, the end of the transfusion. |
| 10 | `BLOOD_UNIT_RES_ID` | NUMERIC |  | Corresponds to the Interfaced information about the scanned unit. |
| 11 | `BLOOD_CODABAR_REG` | VARCHAR |  | The CODABAR registration number from the bag of blood associated with this order. |
| 12 | `IS_BLOOD_YN` | VARCHAR |  | This column will be Yes if this procedure is a prepare or transfuse blood order that uses the transfuse or prepare amount display items. |
| 13 | `TRANSFUSE_AMOUNT` | INTEGER |  | If this is a blood transfusion order, this column is the amount of blood that was ordered. |
| 14 | `TRANSFUSE_AMOUNT_UNIT_C_NAME` | VARCHAR | org | If this is a blood transfusion order, this is the unit in which it was ordered. |
| 15 | `PREPARE_AMOUNT` | INTEGER |  | If this is a blood prepare order, this column is the amount of blood that was ordered. |
| 16 | `PREPARE_AMOUNT_UNIT_C_NAME` | VARCHAR |  | If this is a blood prepare order, this is the unit in which it was ordered. |
| 17 | `WEIGHT_BLD_AMOUNT` | NUMERIC |  | The weight-based amount this blood prepare or transfuse order was placed in. |
| 18 | `WEIGHT_BLD_UNIT_C_NAME` | VARCHAR |  | The weight-based unit this blood prepare or transfuse order was placed in. |
| 19 | `BLOOD_MAIN_ADMIN` | INTEGER |  | The administration line in ORD 11000 holding the main blood details. |
| 20 | `BLOOD_PRODUCT_TYP_C_NAME` | VARCHAR |  | Identify the blood product type when using universal blood procedures. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

