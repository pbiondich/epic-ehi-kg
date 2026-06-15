# OTP_RX_MIXTURE

> The medication mixture information for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 27  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the order template record. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each ingredient in the mixture for the order template in this row. |
| 3 | `MED_MIXTURE_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 4 | `MED_MIXTURE_TYPE_C_NAME` | VARCHAR | org | The ingredient type category ID of a medication in the order template in this row. |
| 5 | `MED_MIXTURE_DOSE` | VARCHAR |  | The dose amount of an ingredient in the mixture for the order template in this row. |
| 6 | `MED_MIXTURE_DUNIT_C_NAME` | VARCHAR | org | The units category ID to use with the dose of the ingredient on this line of the mixture for the order template in this row. |
| 7 | `MED_MIXTURE_FREQ_ID` | VARCHAR |  | The unique identifier of the frequency record of the additive ingredient in the mixture for the order template. |
| 8 | `MED_MIXTURE_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 9 | `MED_MIXTURE_RATE` | VARCHAR |  | The infusion rate of the additive ingredient on this line of the mixture for the order template in this row. |
| 10 | `MED_MIXTURE_RUNIT_C_NAME` | VARCHAR |  | The units category ID to use for the additive ingredient on this line of the mixture for the order template in this row. |
| 11 | `MED_MIXTURE_SPBA_YN` | VARCHAR |  | Indicates whether to use a separate bag for the additive ingredient on this line of the mixture for the order template in this order. 'Y' indicates that the ingredient uses a separate bag. 'N' or Null indicates that the ingredient does not use a separate bag. |
| 12 | `MED_MIXTURE_NONF_YN` | VARCHAR |  | Indicates whether or not the additive ingredient on this line of the mixture for the order template in this row is non-formulary. 'Y' indicates that the ingredient is non-formulary. 'N' indicates that the ingredient is formulary. |
| 13 | `RXM_CALC_DOSE_AMT` | VARCHAR |  | The calculated dose amount for the additive ingredient on this line of the mixture for the order template in this row. |
| 14 | `RXM_CALC_AMT_UNIT_C_NAME` | VARCHAR |  | The units category ID to use with the calculated dose amount for the additive ingredient on this line of the mixture for the order template in this row. |
| 15 | `RXM_DOSE_CALC_INFO` | VARCHAR |  | The dose calculation information for the additive ingredient on this line of the mixture for the order template in this row. |
| 16 | `RXM_ADDS_VOLUME_YN` | VARCHAR |  | Indicates whether or not the additive ingredient on this line of the mixture for the order template in this row adds volume to the mixture. 'Y' indicates that the ingredient adds volume. 'N' or Null indicates that the ingredient does not add volume. |
| 17 | `MED_MIXTURE_SEL_C_NAME` | VARCHAR |  | Indicates how this component is selected when the mixture is ordered. |
| 18 | `MED_MIX_ORIG_DOSE` | VARCHAR |  | The original dose of an ingredient in the order template before it was modified. |
| 19 | `MED_MIX_ORIG_UNIT_C_NAME` | VARCHAR |  | The dose units category ID that correspond to the original dose of the ingredient. |
| 20 | `MED_MIX_PCT_OF_ORIG` | NUMERIC |  | For dose-modified ingredients in a mixture order template, this column shows the percentage ratio of the current dose to the original dose. |
| 21 | `MED_MIX_ORIG_VER_ID` | VARCHAR |  | The unique identifier for the user who last verified the original dose of the ingredient. |
| 22 | `MED_MIX_ORIG_VER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `MED_MIX_OD_VER_DTTM` | DATETIME (Local) |  | The original dose of an ingredient in the order template before it was modified. |
| 24 | `RXM_ROUNDING_ACK_C_NAME` | VARCHAR | org | The acknowledgement reason category ID for the order template given by the user to override a dose rounding warning on this component. |
| 25 | `RXM_SIG` | VARCHAR |  | The component sigs for outpatient intelligent medication selection (IMS) tablet mixtures |
| 26 | `COMPONENT_DISPENSE_TEXT` | VARCHAR |  | This column stores the free text dispense amount. |
| 27 | `COMP_COMPILED_SIG` | VARCHAR |  | This column stores the sigs for each component medication of an outpatient intelligent medication selection (IMS) tablet mixture, including information that is automatically added to the end. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

