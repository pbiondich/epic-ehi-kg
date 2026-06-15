# REFERRAL_PX

> This table contains information on procedures associated with referrals. This table is related to the REFERRAL_ORDER_ID table. The REFERRAL_ORDER_ID table contains the list of procedures for the referral. The REFERRAL_PX table contains information on each of those procedures.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral in database. |
| 2 | `LINE` | INTEGER | PK | The line number of the procedure associated with the referral. For example, if a referral has two associated procedures, the first procedure will have a line value of 1, while the second procedure will have a line value of 2. |
| 3 | `PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `UNITS_REQUESTED` | INTEGER |  | The number of units of this procedure that were requested |
| 5 | `UNITS_APPROVED` | INTEGER |  | The number of units of this procedure that were approved |
| 6 | `TOTAL_PRICE` | NUMERIC |  | The total price calculated for this procedure using fee schedules or vendor contracts (for outgoing referrals) |
| 7 | `NET_PAYABLE` | NUMERIC |  | The total net payable calculated for this procedure (the price - the patient portion). |
| 8 | `PATIENT_PORTION` | NUMERIC |  | The total patient responsibility calculated for this procedure using the benefits engine |
| 9 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `AUTH_REQ_YN` | VARCHAR |  | A flag that indicates whether the member's benefits require a referral for this service. Yes=> a referral is required, No=> a referral is not required. |
| 11 | `COVERED` | VARCHAR |  | A flag that indicates whether the procedure is not covered by the member's benefits or it is covered but by supplemental insurance |
| 12 | `REVENUE_CODE_ID` | NUMERIC |  | Stores the revenue billing code entered on the service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

