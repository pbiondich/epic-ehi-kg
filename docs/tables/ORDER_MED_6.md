# ORDER_MED_6

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_MED_ID`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK | The unique identifier for the medication order record. |
| 2 | `AUTH_SER_ADDRESS_ID` | VARCHAR |  | The unique ID for the address of the order's authorizing provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| 3 | `ORDER_SER_ADDR_ID` | VARCHAR |  | The unique ID for the address of the order's ordering provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| 4 | `SUP_SER_ADDRESS_ID` | VARCHAR |  | The unique ID for the address of the order's supervising provider. It is used to identify an address using the address unique ID (I SER 21000) stored in the provider record. |
| 5 | `TEMP_LONG_TERM_IN_C_NAME` | VARCHAR |  | The category number for the temporary long-term indicator for unsigned orders. |
| 6 | `PRIORITIZED_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the prioritized instant (date and time) for an order in UTC time zone. It represents the most relevant date and time an action was taken on an order. |
| 7 | `PRIORITIZED_INST_DTTM` | DATETIME (Local) |  | This item stores the prioritized instant (date and time) for an order in local time zone. It represents the most relevant date and time an action was taken on an order. |
| 8 | `NEXT_SCH_INST_AT_DISCON_DTTM` | DATETIME (Local) |  | The next scheduled date and time for the order at the time of discontinue. |
| 9 | `NEXT_SCH_AT_DISCON_OFF_SCH_YN` | VARCHAR |  | Indicates whether the next scheduled time of the order at the time of discontinue is off-schedule. 'Y' indicates that the next scheduled time was off-schedule. 'N' or NULL indicate that the next scheduled time was not off-schedule. |
| 10 | `ORD_SIG_HAS_IOU_YN` | VARCHAR |  | Indicates whether Indications of Use are present in the patient sig. 'Y' indicates Indications of Use are present in the patient sig. 'N' or NULL indicate that Indications of Use are not present in the patient sig. |
| 11 | `MED_DIRECTIONS_LONG` | VARCHAR |  | Contains the directions for taking a medication order. |
| 12 | `USER_CHANGED_END_TIME_YN` | VARCHAR |  | Indicates whether the end time is entered by a user. This is only populated for unsigned medication orders. 'Y' indicates the end time is entered by a user. 'N' or NULL indicate that the end time is not entered by a user. |
| 13 | `ORIG_MED_DIRECTIONS_LONG` | VARCHAR |  | Contains the original directions for taking a medication order. |
| 14 | `NO_REIMBURS_CODESET` | VARCHAR |  | Holds the code set of the selected reimbursement code. |
| 15 | `STANDING_COUNT` | INTEGER |  | This item stores a numeric value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. |
| 16 | `STANDING_COUNT_TP_C_NAME` | VARCHAR |  | This count type goes along with the count from ORD-34040 to indicate the number of hours, days, weeks, or occurrences for which the order will take place. |
| 17 | `COUNT_RANGE` | VARCHAR |  | This item stores a ranged value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. Currently only available in Finland. |
| 18 | `COUNT_RANGE_STND_TP_C_NAME` | VARCHAR |  | This ranged count type goes along with the count from ORD-34042 to indicate the number of days, weeks, months, years, or occurrences for which the order will take place. Currently only available in Finland. |
| 19 | `ORDER_START_TM` | DATETIME (Local) |  | The time when the medication order is to start. |
| 20 | `PROTOCOLLED_ORDER_ID` | NUMERIC |  | For an order that was placed from an imaging protocol, this item contains the protocolled imaging procedure order from which the order was placed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

