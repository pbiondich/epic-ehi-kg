# ARPB_TX_REFUND

> This table contains information specific for a refund adjustment, such as refund address information entered on the Refund Request Slip form, and information related to export and import to/from the AP system. Use this table in conjunction with ARPB_TX_REFUND_ADD to display the full address entered on the Refund Request Slip form.

**Primary key:** `TX_ID`  
**Columns:** 26  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | Payment transaction (ETR) ID that was refunded. |
| 2 | `REFUND_ADDR_NAME` | VARCHAR |  | This column contains the name for the refund address entered on the Refund Request Slip form. |
| 3 | `REFUND_ADDR_CITY` | VARCHAR |  | This column contains the city for the refund address entered on the Refund Request Slip form. |
| 4 | `REFUND_ADDR_STATE_C_NAME` | VARCHAR | org | This column contains the state for the refund address entered on the Refund Request Slip form. |
| 5 | `REFUND_ADDR_ZIP` | VARCHAR |  | This column contains the zip code for the refund address entered on the Refund Request Slip form. |
| 6 | `REFUND_ADDR_CUST_C_NAME` | VARCHAR | org | This column contains the custom payee used to override the refund address entered on the Refund Request Slip form. |
| 7 | `REFUND_ADDR_PLN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 8 | `REFUND_ADDR_PYR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 9 | `REFUND_ADDR_CVG_ID` | NUMERIC |  | This column contains the coverage used to override the refund address entered on the Refund Request Slip form. |
| 10 | `REFUND_AP_EXPORT_DT` | DATETIME |  | Date when the refund adjustment was exported to the Accounts Payable (AP) system |
| 11 | `REFUND_AP_IMPORT_DT` | DATETIME |  | Date when information was imported from Accounts Payable (AP) system to confirm a refund |
| 12 | `REFUND_CHECK_NUM` | VARCHAR |  | Check number for AP check produced as result of refund adjustment. |
| 13 | `REFUND_CHECK_AMT` | NUMERIC |  | Check amount for AP check produced as result of refund adjustment. |
| 14 | `REFUND_CHECK_DT` | DATETIME |  | Check date for AP check produced as result of refund adjustment. |
| 15 | `REFUND_COMMENT` | VARCHAR |  | Contains free text comment, with information related to a refund, imported from the Accounts Payable (AP) system |
| 16 | `REFUND_ACC_USR_ID` | VARCHAR |  | This column contains the user that accepted the Refund Request Slip form. |
| 17 | `REFUND_ACC_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `REFUND_ADDR_EMP_ID` | VARCHAR |  | This column contains the user that overrode the refund address entered on the Refund Request Slip form. |
| 19 | `REFUND_ADDR_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `REFUND_ADDR_CNTY_C_NAME` | VARCHAR | org | The refund address county category ID for the transaction. |
| 21 | `REFUND_ADDR_CNTRY_C_NAME` | VARCHAR | org | The refund address country category ID for the transaction. |
| 22 | `REFUND_ADDR_HNUM` | VARCHAR |  | Refund address house number |
| 23 | `REFUND_ADDR_DIST_C_NAME` | VARCHAR | org | The refund address district category ID for the transaction. |
| 24 | `REFUND_FORCED_YN` | VARCHAR |  | If set to yes, this item indicates that the refund has been force posted or rejected (despite not having received import information from the AP system). This is only for use when refunds are held pending AP import. |
| 25 | `REFUND_ADDR_CUST_PAYEE_ID` | VARCHAR |  | Stores the ID of the custom payee to send the refund to. |
| 26 | `REFUND_ADDR_CUST_PAYEE_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

