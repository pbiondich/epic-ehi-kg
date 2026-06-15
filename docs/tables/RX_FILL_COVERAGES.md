# RX_FILL_COVERAGES

> This table contains the coverages used for prescription fills. A given fill can have multiple coverages associated with it. Other clinical information about the fill is in table ORDER_DISP_INFO.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `RX_COVERAGES_ID` | NUMERIC |  | The unique identifier for the list of coverage records used for the prescription fill. |
| 7 | `PAYOR_PAY_AMOUNT` | NUMERIC |  | This is the amount each payor is responsible for on a prescription. |
| 8 | `RX_ACCTS_ID` | NUMERIC |  | The unique identifier of the guarantor account to use for any outstanding prescription balances on the order. It is populated in one of two ways. If a personal/family coverage is chosen in order entry, then a guarantor account (in the Pickup Pharmacy's service area) attached to that coverage will be used. Or, if an account of a type other than personal/family is selected (for example, workers' comp), then that guarantor account will be used. |
| 9 | `PLAN_PRICE_FOR_CVG` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This column is the coverage-specific plan price for the fill. This will be sent in to the payor during adjudication or used when billing charity or discount coverages. |
| 10 | `PAYER_TAX_DUE` | NUMERIC |  | This is the rounded tax amount each payer is responsible for on a prescription. This is used for UAE billing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

