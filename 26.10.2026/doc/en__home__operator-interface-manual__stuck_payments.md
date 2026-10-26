On this page, you can find a list of errors related to stuck payments. If the error you see on a payment is not described here, please contact your account manager for further details.


| Error | Value | Resolution | 
| 
 
 | Insufficient funds on the payment method balance for processing. | You need to contact your account manager to submit a top-up request. | 
| `Unexpected token at` | System error | Payments can be canceled in the operator interface so that the affiliate can request a withdrawal again. | 
| 
 | ||
| `COUNTRY_BLOCKED_FOR_PAYMENTS` | Payout to the user’s country is blocked. | The payment should be canceled. The affiliate is advised to choose another payment method. | 
| `THE_RECIPIENTS_ACCOUNT_CANNOT``_RECEIVE_PAYMENTS` | The affiliate’s Skrill account is likely unverified, limited, or blocked from receiving funds. | The payment should be canceled. Affiliates are advised to contact the payment system for clarification or choose an alternative payment method. | 
| `DISALLOWED_CROSS_REGION_``PAYMENT (area: eea or row)` | The payout specifies an incorrect Skrill zone. | The payment should be canceled. The affiliate can request a withdrawal by specifying the correct zone for their account. | 
| `DISALLOWED_CROSS_REGION_``PAYMENT (no area)` | The payout request is missing both `eea`or`row`in the`area `block. This error occurs because specifying a zone is mandatory. | The payment should be canceled. The affiliate can request a withdrawal by specifying the correct zone for their account. | 
| `INVALID_EMAIL` | An incorrect email is provided in the payout. | The payment should be canceled. The affiliate can request a withdrawal by providing the correct email for their account. | 
| `GENERIC_ERROR` | The payment is incorrectly processed by the payment provider for other reasons. | The payment should be canceled. The affiliate can request the payment after verifying the wallet details. | 
| 
 | ||
| `PaymentService: RollbackPayment` | Internal error. | You need to contact the account manager for clarification on the payment details. | 
| `Unable to exchange the requested amount at the moment. Specify a smaller amount or try again later.` | Internal error. | The payment should be canceled, and the withdrawal should be requested again. | 
| `The foreign id has already been taken` | The specified foreign ID of the transaction is already being processed. | The payment should be canceled, and the withdrawal should be requested again. | 
| `Invalid USDTT or USDTE address` | An incorrect protocol is specified in the payment. | In the affiliate interface, when selecting Crypto to add a USDT wallet, there are two options: USDTT refers to the USDT TRC20 walletUSDTE refers to the USDT ERC20 wallet.
 The payment should be canceled. The affiliate needs to provide the wallet details with the correct protocol and request the payout again. | 
| 
 
 
 | The transaction amount is below the minimum allowed. | The payment should be canceled. A new payment should be requested with an amount above the limit set by the payment system. | 
| `Invalid LTC, BTC etc. address` | An incorrect wallet address is specified in the payment. | The payment should be canceled. The affiliate needs to add the correct wallet details and request the withdrawal again. | 
| 
 | ||
| No error code | Internal error. | You need to contact the account manager for clarification on the payment with the specified error. | 
| `COUNTRY_BLOCKED_FOR_PAYMENTS` | The transaction is declined by the payment provider – the user’s country is blocked. | The payment should be canceled. The affiliate is advised to choose another payment method. |