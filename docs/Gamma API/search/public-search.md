# Search markets, events, and profiles

## 接口名称
Search markets, events, and profiles

## 请求方法
GET

## Endpoint（完整路径）
https://gamma-api.polymarket.com/public-search

---

## 请求参数（Query Parameters）

> 说明：以下参数的“说明”字段，若页面未给出明确解释，则标记为「页面未注明」。

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| q | string | 是 | 页面未注明 |
| cache | boolean | 否 | 页面未注明 |
| events_status | string | 否 | 页面未注明 |
| limit_per_type | integer | 否 | 页面未注明 |
| page | integer | 否 | 页面未注明 |
| events_tag | string[] | 否 | 页面未注明 |
| keep_closed_markets | integer | 否 | 页面未注明 |
| sort | string | 否 | 页面未注明 |
| ascending | boolean | 否 | 页面未注明 |
| search_tags | boolean | 否 | 页面未注明 |
| search_profiles | boolean | 否 | 页面未注明 |
| recurrence | string | 否 | 页面未注明 |
| exclude_tag_id | integer[] | 否 | 页面未注明 |
| optimized | boolean | 否 | 页面未注明 |

---

## 返回参数（Response 200 - application/json）

### 顶层结构

| 字段名 | 类型 | 说明 |
|---|---|---|
| events | object[] \| null | 页面未注明 |
| tags | object[] \| null | 页面未注明 |
| profiles | object[] \| null | 页面未注明 |
| pagination | object | 页面未注明 |

---

### events[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| ticker | string | 页面未注明 |
| slug | string | 页面未注明 |
| title | string | 页面未注明 |
| subtitle | string | 页面未注明 |
| description | string | 页面未注明 |
| resolutionSource | string | 页面未注明 |
| startDate | string (date-time) | 页面未注明 |
| creationDate | string (date-time) | 页面未注明 |
| endDate | string (date-time) | 页面未注明 |
| image | string | 页面未注明 |
| icon | string | 页面未注明 |
| active | boolean | 页面未注明 |
| closed | boolean | 页面未注明 |
| archived | boolean | 页面未注明 |
| new | boolean | 页面未注明 |
| featured | boolean | 页面未注明 |
| restricted | boolean | 页面未注明 |
| liquidity | integer | 页面未注明 |
| volume | integer | 页面未注明 |
| openInterest | integer | 页面未注明 |
| sortBy | string | 页面未注明 |
| category | string | 页面未注明 |
| subcategory | string | 页面未注明 |
| isTemplate | boolean | 页面未注明 |
| templateVariables | string | 页面未注明 |
| published_at | string | 页面未注明 |
| createdBy | string | 页面未注明 |
| updatedBy | string | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| commentsEnabled | boolean | 页面未注明 |
| competitive | integer | 页面未注明 |
| volume24hr | integer | 页面未注明 |
| volume1wk | integer | 页面未注明 |
| volume1mo | integer | 页面未注明 |
| volume1yr | integer | 页面未注明 |
| featuredImage | string | 页面未注明 |
| disqusThread | string | 页面未注明 |
| parentEvent | string | 页面未注明 |
| enableOrderBook | boolean | 页面未注明 |
| liquidityAmm | integer | 页面未注明 |
| liquidityClob | integer | 页面未注明 |
| negRisk | boolean | 页面未注明 |
| negRiskMarketID | string | 页面未注明 |
| negRiskFeeBips | integer | 页面未注明 |
| commentCount | integer | 页面未注明 |
| imageOptimized | object | 页面未注明 |
| iconOptimized | object | 页面未注明 |
| featuredImageOptimized | object | 页面未注明 |
| subEvents | string[] | 页面未注明 |
| markets | object[] | 页面未注明 |
| series | object[] | 页面未注明 |
| categories | object[] | 页面未注明 |
| collections | object[] | 页面未注明 |
| tags | object[] | 页面未注明 |
| cyom | boolean | 页面未注明 |
| closedTime | string (date-time) | 页面未注明 |
| showAllOutcomes | boolean | 页面未注明 |
| showMarketImages | boolean | 页面未注明 |
| automaticallyResolved | boolean | 页面未注明 |
| enableNegRisk | boolean | 页面未注明 |
| automaticallyActive | boolean | 页面未注明 |
| eventDate | string | 页面未注明 |
| startTime | string (date-time) | 页面未注明 |
| eventWeek | integer | 页面未注明 |
| seriesSlug | string | 页面未注明 |
| score | string | 页面未注明 |
| elapsed | string | 页面未注明 |
| period | string | 页面未注明 |
| live | boolean | 页面未注明 |
| ended | boolean | 页面未注明 |
| finishedTimestamp | string (date-time) | 页面未注明 |
| gmpChartMode | string | 页面未注明 |
| eventCreators | object[] | 页面未注明 |
| tweetCount | integer | 页面未注明 |
| chats | object[] | 页面未注明 |
| featuredOrder | integer | 页面未注明 |
| estimateValue | boolean | 页面未注明 |
| cantEstimate | boolean | 页面未注明 |
| estimatedValue | string | 页面未注明 |
| templates | object[] | 页面未注明 |
| spreadsMainLine | integer | 页面未注明 |
| totalsMainLine | integer | 页面未注明 |
| carouselMap | string | 页面未注明 |
| pendingDeployment | boolean | 页面未注明 |
| deploying | boolean | 页面未注明 |
| deployingTimestamp | string (date-time) | 页面未注明 |
| scheduledDeploymentTimestamp | string (date-time) | 页面未注明 |
| gameStatus | string | 页面未注明 |

---

#### — imageOptimized（object）
（同结构也适用于：iconOptimized、featuredImageOptimized、profiles[].profileImageOptimized、collections[].imageOptimized 等）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| imageUrlSource | string | 页面未注明 |
| imageUrlOptimized | string | 页面未注明 |
| imageSizeKbSource | integer | 页面未注明 |
| imageSizeKbOptimized | integer | 页面未注明 |
| imageOptimizedComplete | boolean | 页面未注明 |
| imageOptimizedLastUpdated | string | 页面未注明 |
| relID | integer | 页面未注明 |
| field | string | 页面未注明 |
| relname | string | 页面未注明 |

---

#### — markets[]（object）
> 注意：这是 events[].markets[] 的市场对象结构（页面示例中给出了非常多字段）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| question | string | 页面未注明 |
| conditionId | string | 页面未注明 |
| slug | string | 页面未注明 |
| twitterCardImage | string | 页面未注明 |
| resolutionSource | string | 页面未注明 |
| endDate | string (date-time) | 页面未注明 |
| category | string | 页面未注明 |
| ammType | string | 页面未注明 |
| liquidity | string | 页面未注明 |
| sponsorName | string | 页面未注明 |
| sponsorImage | string | 页面未注明 |
| startDate | string (date-time) | 页面未注明 |
| xAxisValue | string | 页面未注明 |
| yAxisValue | string | 页面未注明 |
| denominationToken | string | 页面未注明 |
| fee | string | 页面未注明 |
| image | string | 页面未注明 |
| icon | string | 页面未注明 |
| lowerBound | string | 页面未注明 |
| upperBound | string | 页面未注明 |
| description | string | 页面未注明 |
| outcomes | string | 页面未注明 |
| outcomePrices | string | 页面未注明 |
| volume | string | 页面未注明 |
| active | boolean | 页面未注明 |
| marketType | string | 页面未注明 |
| formatType | string | 页面未注明 |
| lowerBoundDate | string | 页面未注明 |
| upperBoundDate | string | 页面未注明 |
| closed | boolean | 页面未注明 |
| marketMakerAddress | string | 页面未注明 |
| createdBy | integer | 页面未注明 |
| updatedBy | integer | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| closedTime | string | 页面未注明 |
| wideFormat | boolean | 页面未注明 |
| new | boolean | 页面未注明 |
| mailchimpTag | string | 页面未注明 |
| featured | boolean | 页面未注明 |
| archived | boolean | 页面未注明 |
| resolvedBy | string | 页面未注明 |
| restricted | boolean | 页面未注明 |
| marketGroup | integer | 页面未注明 |
| groupItemTitle | string | 页面未注明 |
| groupItemThreshold | string | 页面未注明 |
| questionID | string | 页面未注明 |
| umaEndDate | string | 页面未注明 |
| enableOrderBook | boolean | 页面未注明 |
| orderPriceMinTickSize | integer | 页面未注明 |
| orderMinSize | integer | 页面未注明 |
| umaResolutionStatus | string | 页面未注明 |
| curationOrder | integer | 页面未注明 |
| volumeNum | integer | 页面未注明 |
| liquidityNum | integer | 页面未注明 |
| endDateIso | string | 页面未注明 |
| startDateIso | string | 页面未注明 |
| umaEndDateIso | string | 页面未注明 |
| hasReviewedDates | boolean | 页面未注明 |
| readyForCron | boolean | 页面未注明 |
| commentsEnabled | boolean | 页面未注明 |
| volume24hr | integer | 页面未注明 |
| volume1wk | integer | 页面未注明 |
| volume1mo | integer | 页面未注明 |
| volume1yr | integer | 页面未注明 |
| gameStartTime | string | 页面未注明 |
| secondsDelay | integer | 页面未注明 |
| clobTokenIds | string | 页面未注明 |
| disqusThread | string | 页面未注明 |
| shortOutcomes | string | 页面未注明 |
| teamAID | string | 页面未注明 |
| teamBID | string | 页面未注明 |
| umaBond | string | 页面未注明 |
| umaReward | string | 页面未注明 |
| fpmmLive | boolean | 页面未注明 |
| volume24hrAmm | integer | 页面未注明 |
| volume1wkAmm | integer | 页面未注明 |
| volume1moAmm | integer | 页面未注明 |
| volume1yrAmm | integer | 页面未注明 |
| volume24hrClob | integer | 页面未注明 |
| volume1wkClob | integer | 页面未注明 |
| volume1moClob | integer | 页面未注明 |
| volume1yrClob | integer | 页面未注明 |
| volumeAmm | integer | 页面未注明 |
| volumeClob | integer | 页面未注明 |
| liquidityAmm | integer | 页面未注明 |
| liquidityClob | integer | 页面未注明 |
| makerBaseFee | integer | 页面未注明 |
| takerBaseFee | integer | 页面未注明 |
| customLiveness | integer | 页面未注明 |
| acceptingOrders | boolean | 页面未注明 |
| notificationsEnabled | boolean | 页面未注明 |
| score | integer | 页面未注明 |
| imageOptimized | object | 页面未注明 |
| iconOptimized | object | 页面未注明 |
| events | array | 页面示例值为 `"<array>"`（未展开） |
| categories | object[] | 页面未注明 |
| tags | object[] | 页面未注明 |
| creator | string | 页面未注明 |
| ready | boolean | 页面未注明 |
| funded | boolean | 页面未注明 |
| pastSlugs | string | 页面未注明 |
| readyTimestamp | string (date-time) | 页面未注明 |
| fundedTimestamp | string (date-time) | 页面未注明 |
| acceptingOrdersTimestamp | string (date-time) | 页面未注明 |
| competitive | integer | 页面未注明 |
| rewardsMinSize | integer | 页面未注明 |
| rewardsMaxSpread | integer | 页面未注明 |
| spread | integer | 页面未注明 |
| automaticallyResolved | boolean | 页面未注明 |
| oneDayPriceChange | integer | 页面未注明 |
| oneHourPriceChange | integer | 页面未注明 |
| oneWeekPriceChange | integer | 页面未注明 |
| oneMonthPriceChange | integer | 页面未注明 |
| oneYearPriceChange | integer | 页面未注明 |
| lastTradePrice | integer | 页面未注明 |
| bestBid | integer | 页面未注明 |
| bestAsk | integer | 页面未注明 |
| automaticallyActive | boolean | 页面未注明 |
| clearBookOnStart | boolean | 页面未注明 |
| chartColor | string | 页面未注明 |
| seriesColor | string | 页面未注明 |
| showGmpSeries | boolean | 页面未注明 |
| showGmpOutcome | boolean | 页面未注明 |
| manualActivation | boolean | 页面未注明 |
| negRiskOther | boolean | 页面未注明 |
| gameId | string | 页面未注明 |
| groupItemRange | string | 页面未注明 |
| sportsMarketType | string | 页面未注明 |
| line | integer | 页面未注明 |
| umaResolutionStatuses | string | 页面未注明 |
| pendingDeployment | boolean | 页面未注明 |
| deploying | boolean | 页面未注明 |
| deployingTimestamp | string (date-time) | 页面未注明 |
| scheduledDeploymentTimestamp | string (date-time) | 页面未注明 |
| rfqEnabled | boolean | 页面未注明 |
| eventStartTime | string (date-time) | 页面未注明 |

---

#### — categories[]（object）
（events[].categories[] 与 events[].markets[].categories[] 均出现该结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| label | string | 页面未注明 |
| parentCategory | string | 页面未注明 |
| slug | string | 页面未注明 |
| publishedAt | string | 页面未注明 |
| createdBy | string | 页面未注明 |
| updatedBy | string | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |

---

#### — tags[]（object）
（events[].tags[] 与 events[].markets[].tags[] 均出现该结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| label | string | 页面未注明 |
| slug | string | 页面未注明 |
| forceShow | boolean | 页面未注明 |
| publishedAt | string | 页面未注明 |
| createdBy | integer | 页面未注明 |
| updatedBy | integer | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| forceHide | boolean | 页面未注明 |
| isCarousel | boolean | 页面未注明 |

---

#### — collections[]（object）
（events[].collections[] 与 series[].collections[] 均出现）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| ticker | string | 页面未注明 |
| slug | string | 页面未注明 |
| title | string | 页面未注明 |
| subtitle | string | 页面未注明 |
| collectionType | string | 页面未注明 |
| description | string | 页面未注明 |
| tags | string | 页面未注明 |
| image | string | 页面未注明 |
| icon | string | 页面未注明 |
| headerImage | string | 页面未注明 |
| layout | string | 页面未注明 |
| active | boolean | 页面未注明 |
| closed | boolean | 页面未注明 |
| archived | boolean | 页面未注明 |
| new | boolean | 页面未注明 |
| featured | boolean | 页面未注明 |
| restricted | boolean | 页面未注明 |
| isTemplate | boolean | 页面未注明 |
| templateVariables | string | 页面未注明 |
| publishedAt | string | 页面未注明 |
| createdBy | string | 页面未注明 |
| updatedBy | string | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| commentsEnabled | boolean | 页面未注明 |
| imageOptimized | object | 页面未注明 |
| iconOptimized | object | 页面未注明 |
| headerImageOptimized | object | 页面未注明 |

---

#### — series[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| ticker | string | 页面未注明 |
| slug | string | 页面未注明 |
| title | string | 页面未注明 |
| subtitle | string | 页面未注明 |
| seriesType | string | 页面未注明 |
| recurrence | string | 页面未注明 |
| description | string | 页面未注明 |
| image | string | 页面未注明 |
| icon | string | 页面未注明 |
| layout | string | 页面未注明 |
| active | boolean | 页面未注明 |
| closed | boolean | 页面未注明 |
| archived | boolean | 页面未注明 |
| new | boolean | 页面未注明 |
| featured | boolean | 页面未注明 |
| restricted | boolean | 页面未注明 |
| isTemplate | boolean | 页面未注明 |
| templateVariables | boolean | 页面示例为 `true` |
| publishedAt | string | 页面未注明 |
| createdBy | string | 页面未注明 |
| updatedBy | string | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| commentsEnabled | boolean | 页面未注明 |
| competitive | string | 页面未注明 |
| volume24hr | integer | 页面未注明 |
| volume | integer | 页面未注明 |
| liquidity | integer | 页面未注明 |
| startDate | string (date-time) | 页面未注明 |
| pythTokenID | string | 页面未注明 |
| cgAssetName | string | 页面未注明 |
| score | integer | 页面未注明 |
| events | array | 页面示例值为 `"<array>"`（未展开） |
| collections | object[] | 页面未注明 |

---

#### — eventCreators[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| creatorName | string | 页面未注明 |
| creatorHandle | string | 页面未注明 |
| creatorUrl | string | 页面未注明 |
| creatorImage | string | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |

---

#### — chats[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| channelId | string | 页面未注明 |
| channelName | string | 页面未注明 |
| channelImage | string | 页面未注明 |
| live | boolean | 页面未注明 |
| startTime | string (date-time) | 页面未注明 |
| endTime | string (date-time) | 页面未注明 |

---

#### — templates[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| eventTitle | string | 页面未注明 |
| eventSlug | string | 页面未注明 |
| eventImage | string | 页面未注明 |
| marketTitle | string | 页面未注明 |
| description | string | 页面未注明 |
| resolutionSource | string | 页面未注明 |
| negRisk | boolean | 页面未注明 |
| sortBy | string | 页面未注明 |
| showMarketImages | boolean | 页面未注明 |
| seriesSlug | string | 页面未注明 |
| outcomes | string | 页面未注明 |

---

### tags[]（顶层 tags，object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| label | string | 页面未注明 |
| slug | string | 页面未注明 |
| event_count | integer | 页面未注明 |

---

### profiles[]（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| id | string | 页面未注明 |
| name | string | 页面未注明 |
| user | integer | 页面未注明 |
| referral | string | 页面未注明 |
| createdBy | integer | 页面未注明 |
| updatedBy | integer | 页面未注明 |
| createdAt | string (date-time) | 页面未注明 |
| updatedAt | string (date-time) | 页面未注明 |
| utmSource | string | 页面未注明 |
| utmMedium | string | 页面未注明 |
| utmCampaign | string | 页面未注明 |
| utmContent | string | 页面未注明 |
| utmTerm | string | 页面未注明 |
| walletActivated | boolean | 页面未注明 |
| pseudonym | string | 页面未注明 |
| displayUsernamePublic | boolean | 页面未注明 |
| profileImage | string | 页面未注明 |
| bio | string | 页面未注明 |
| proxyWallet | string | 页面未注明 |
| profileImageOptimized | object | 页面未注明 |
| isCloseOnly | boolean | 页面未注明 |
| isCertReq | boolean | 页面未注明 |
| certReqDate | string (date-time) | 页面未注明 |

---

### pagination（object）

| 字段名 | 类型 | 说明 |
|---|---|---|
| hasMore | boolean | 页面未注明 |
| totalResults | integer | 页面未注明 |