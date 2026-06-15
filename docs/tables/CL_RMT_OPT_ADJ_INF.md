# CL_RMT_OPT_ADJ_INF

> This table contains outpatient adjudication information from the Image Database (IMD) master file.

**Primary key:** `IMAGE_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with outpatient adjudication information. |
| 2 | `REIMBURSEMENT_RATE` | NUMERIC |  | The reimbursement rate percentage expressed as a decimal for outpatient adjudication info. |
| 3 | `HCPCS_PAYABLE_AMT` | NUMERIC |  | Monetary amount for the claim Healthcare Common Procedure Coding System (HCPCS) payable amount for outpatient adjudication info. |
| 4 | `OUTPAT_REMARK_1` | VARCHAR |  | Outpatient adjudication remark code 1. |
| 5 | `OUTPAT_REMARK_2` | VARCHAR |  | Outpatient adjudication remark code 2. |
| 6 | `OUTPAT_REMARK_3` | VARCHAR |  | Outpatient adjudication remark code 3. |
| 7 | `OUTPAT_REMARK_4` | VARCHAR |  | Outpatient adjudication remark code 4. |
| 8 | `OUTPAT_REMARK_5` | VARCHAR |  | Outpatient adjudication remark code 5. |
| 9 | `CLAIM_ESRD_PAY_AMT` | NUMERIC |  | End stage renal disease (ESRD) payment amount for outpatient adjudication info. |
| 10 | `OUT_NONPAY_PRF_AMT` | NUMERIC |  | Monetary amount for outpatient adjudication nonpayable professional component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

