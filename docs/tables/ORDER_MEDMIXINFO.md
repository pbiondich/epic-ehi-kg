# ORDER_MEDMIXINFO

> This table is used to extract ingredient medication information for mixture orders.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 33  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. Each line represents an ingredient of the mixture. |
| 3 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 4 | `INGREDIENT_TYPE_C_NAME` | VARCHAR | org | The ingredient type category ID for an ingredient of a medication mixture, indicating what the type of ingredient such as medication or base. |
| 5 | `MIN_DOSE_AMOUNT` | NUMERIC |  | The minimum ordered dose amount of the ingredient. |
| 6 | `MAX_DOSE_AMOUNT` | NUMERIC |  | The maximum ordered dose amount of the ingredient. |
| 7 | `DOSE_UNIT_C_NAME` | VARCHAR | org | The med & dose unit category ID for an ingredient of a medication mixture. |
| 8 | `FREQUENCY_ID` | VARCHAR |  | The unique identifier of the frequency record associated with the mixture ingredient. |
| 9 | `FREQUENCY_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 10 | `MIN_INFUSION_RATE` | NUMERIC |  | The minimum infusion rate amount of the ingredient. |
| 11 | `MAX_INFUSION_RATE` | NUMERIC |  | The maximum infusion rate amount of the ingredient. |
| 12 | `RATE_UNIT_C_NAME` | VARCHAR |  | The infusion rate unit for the ingredient. |
| 13 | `SEPARATE_BAG_YN` | VARCHAR |  | Indicates that the ingredient is in a separated bag. 'Y' indicates that the ingredient is in a separated bag. 'N' or NULL indicates that the ingredient is not in a separated bag. |
| 14 | `NONFORMULARY_YN` | VARCHAR |  | Indicates whether the ingredient is not on a hospital formulary. 'Y' indicates that the ingredient is not on a hospital formulary. 'N' or NULL indicates that the ingredient is on a hospital formulary. |
| 15 | `SELECTION` | VARCHAR |  | Indicates the selection status of the ingredient. |
| 16 | `MIN_CALC_DOSE_AMT` | NUMERIC |  | Indicates the minimum calculated dose amount for the ingredient. |
| 17 | `MAX_CALC_DOSE_AMT` | NUMERIC |  | Indicates the maximum calculated dose amount for the ingredient. |
| 18 | `CALC_DOSE_UNIT_C_NAME` | VARCHAR |  | The med & dose unit category ID for the calculated dose of the medication order. |
| 19 | `DOSE_CALC_INFO` | VARCHAR |  | Indicates the calculated steps to get the calculated minimum or maximum calculated dose. |
| 20 | `CALCDOSAMT_PDAY` | NUMERIC |  | Calculated dose amount per day. |
| 21 | `RXM_CALC_AMTUNTPD_C_NAME` | VARCHAR |  | Unit for calculated dose amount per day. |
| 22 | `RXM_ADDS_VOLUME_YN` | VARCHAR |  | Indicates whether the ingredient adds volume to the mixture. 'Y' indicates that the ingredient does contribute volume to the mixture. 'N' or NULL indicates that the ingredient does not contribute volume to the mixture. |
| 23 | `DOSE_CALC_WARNING` | VARCHAR |  | A warning about whether a medication mixture's final dose was rounded by more than a specified percentage. |
| 24 | `RXM_ADDS_WT_YN` | VARCHAR |  | Indicates whether the ingredient adds weight to the mixture. 'Y' indicates that the ingredient does contribute weight to the mixture. 'N' or NULL indicates that the ingredient does not contribute weight to the mixture. |
| 25 | `RXM_DISP_QTY` | NUMERIC |  | Stores the ordered dispense quantity. |
| 26 | `RXM_DISP_UNIT_C_NAME` | VARCHAR |  | Stores the ordered ingredient dispense quantity unit. |
| 27 | `RXM_RATIO` | NUMERIC |  | Stores ingredient ratio. |
| 28 | `RXM_RATIO_UNIT_C_NAME` | VARCHAR |  | Stores the ingredient ratio unit. |
| 29 | `RXM_DOSE_RND_ACK_C_NAME` | VARCHAR | org | The category number for the acknowledgement reason given by the user to override a dose rounding warning on this component. |
| 30 | `COMP_RX_NUM_RAW` | VARCHAR |  | The unformatted prescription numbers for each component in a medication that should be administered with multiple tablets of different strengths. |
| 31 | `COMP_RX_NUM_FMT` | VARCHAR |  | The formatted prescription numbers for each component in a medication that should be administered with multiple tablets of different strengths. |
| 32 | `COMP_SIG` | VARCHAR |  | The medication instructions for a single component of a mixture comprised of multiple medications with different tablet strengths. |
| 33 | `COMP_DISPENSE_TEXT` | VARCHAR |  | This column stores the dispense amount added by a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

