# Jay's Daily Coding-Related Activities

_Generated 2026-09-15 07:01 CDT · timezone America/Chicago_

Sources: merged PRs, issues opened/closed, effort-board bullets (`docs/EFFORT-LOG.md`).
Agent names are stripped from titles; HTML site shows logos instead.

- **HTML:** https://jaywedgeworth22.github.io/ai-fleet-coordinator/
- **ICS (daily outline):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/daily-digest.ics
- **ICS (per-commit activity):** https://jaywedgeworth22.github.io/ai-fleet-coordinator/calendar/agent-activity.ics

## 2026-09-15

*0 PRs merged · 0 issues opened · 0 issues closed · 238 effort rows*

### Effort board

- **ST** `Grok` Land remaining OPEN ST PRs to main — IN PROGRESS 2026-09-15 (board `c6ee03aa`). #3284 Qdrant fuse P1s on this branch. Squash auto-merge, no Coolify Deploy
- **ST** `Grok` Land remaining OPEN ST PRs to main — IN PROGRESS 2026-09-15 (board `c6ee03aa`, worktree `~/apps/trading — sweep`). Squash auto-merge, no ` — admin`, no Coolify Deploy. One-at-a-time because of P0 `fbf9bb2e`
- **ST** `Grok` Land remaining OPEN ST PRs to main — IN PROGRESS 2026-09-15 (board `c6ee03aa`). #3296 401 JSON redirect fix on this branch. Squash auto-merge, no Coolify Deploy
- **ST** `Antigravity` `Grok` Event-loop stall elimination from synchronous `logApiHealth` pruning & scheduler watchdog AbortController — IN PR 2026-09-15 (issue #3221, PR #3282, — review-thread fixes). Buffered `api_health_log` insertions in memory and flush in 5-second batches (or at 50 rows) to stop synchronous SQLite main-thread freezes on outbound API calls; conditionally executed retention pru
- **ST** `Antigravity` Alpaca-trade-api v4 SDK migration & adapter modernization — PLANNED (owner directive). Migrate `src/lib/alpaca.ts` from `@alpacahq/alpaca-trade-api` v3 flat client to v4 namespace API (`trading.`, `marketData.`), update response mappers to handle camelCase properties (`accountNumber`, `portfolioValue`, `avgEntryPrice`, `bidPrice`/`askPrice`), update order placement/canc
- **ST** `Claude` Durable litestream remote-inventory cache (PR #2665 leftover) — IN PROGRESS. Issue #2694
- **ST** `Claude` Durable litestream remote-inventory cache (PR #2665 leftover) — IN PROGRESS. Issue #2694
- **ST** `Codex` Wire the getRedTeamEfficacy scorecard into the console — DEPLOYED
- **ST** `Codex` Batch typed-confirm flow for LIVE proposals in approvals triage
- **ST** `Claude` PR #1095 inline-Bear bare-array recovery + #1097 docs close-out
- **ST** `Grok` Prefer Pushover over Resend — COMPLETED via #2698. Litestream-wedge remainder is not this lane. Issue #2697 first line preserved historically
- **ST** `Claude` Durable litestream remote-inventory cache — COMPLETED. Issue #2694 closed
- **ST** #838/#837/#1319 via PR #2459 (prompt fencing, headline first-seen, approval 4xx)
- **ST** P2.4 congress_share_daily: 60m failure backoff + activeDailySharePromise single-flight already on main; residual outer IfDue single-flight in residual PR
- **ST** P2.6 order_placement_uncertain → #2459 / strategy placement classification
- **ST** P2.9 LLM failover + scheduler jitter already wired; UI exposes llmFallbackModels (seeding remains owner decision #1324)
- **ST** P3 feed coalesce, KNOWN_GLOBAL System-wide, storage_warning type, evidence_age LRU, protective-stop attribution largely on main
- **ST** Console topCandidates.slice crash fixed via safeTopCandidates on main
- **ST** iOS Coach → Insights rename already on main (InsightsView)
- **ST** Merged PRs closed as DEPLOYED on board: #2488 framework reopen, #2450 Run once A6, #2442 TestFlight ship, #2429 congress filing skill, #2413 plain nav B1, #2398 no direct FMP/Quiver/UW, #2444 auto-pause
- **ST** `Codex` SEC/RAG P0 occurrence identity + durable manifest/job state ( program; RAG-B03/B06/B07)
- **ST** `Codex` SEC/RAG P1 retrieval/strategy consumption redesign ( program; RAG-B11/B12/B13/B18)
- **ST** `Cursor` `Antigravity` ~~Disentangle PR #805: land — P0/P1 commit and — health slice as separate merges
- **ST** `Cursor` ~~Migrate legacy regime:current row to per-user keys at first tick after the P0 fix lands
- **ST** Resolve main-protection ruleset review gate that leaves all-green PRs stuck BLOCKED (OWNER, S)
- **ST** `Claude` check-pin required-status-context merge deadlock fix (branch
- **ST** `Cursor` Corpus re-embed scoped-run purge gate fix (branch
- **ST** `Cursor` Stop placement intent authoritative-absence fix (branch
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. DB evaluator and Pinecone hosted-inference benchmark are locally committed; focused tests, scoped lint, TypeScript, and diff-check are green. Parent integration/PR remains pending. Both paths are bounded a
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. DB evaluator and Pinecone hosted-inference benchmark are locally committed; benchmark follow-up adds empty-set refusal, absolute CLI spend caps, model-default reranking, and provider usage receipts. Focuse
- **ST** `Claude` BRANCH PROTECTION TEMPORARILY RELAXED to break a 34-PR merge deadlock
- **ST** `Claude` CI-load trim: Playwright Smoke off every PR (worktree `ci-trim-smoke`
- **ST** `Claude` Which-key visibility + "agents never create API keys" ruling (worktree
- **ST** `Claude` `Codex` PR #1776 review-thread closeout: all 4 — findings fixed
- **ST** `Claude` Three new RapidAPI-backed enrichment providers: Mboum Finance, YH
- **ST** `Claude` Which-key visibility + "agents never create API keys" ruling (worktree
- **ST** `Claude` Usage-compliance Wave 2 (ST lane): telemetry gaps + OpenRouter classifier
- **ST** `Antigravity` `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` `Antigravity` [ on 's lane] PR #1775 review-thread closeout — scoped re-embed progress
- **ST** `Antigravity` `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` handoff §7 ports: coach-note archive + coach-note/lesson vector writers
- **ST** `Claude` OpenRouter credit signal on /api/health (branch `monet/openrouter-credit-health`
- **ST** `outcome-engine` — outcome writer (matured outcomes onto decision cases), multi-horizon
- **ST** `episodic-retrieval` — new `experience-memory.ts`: decision-time k-NN analogs +
- **ST** `coaching-durable` — coach notes through `ingestLearned` (origin `coach`), kill the silent
- **ST** `reflection-decompose` — done, pushed, awaiting the landing train (branch
- **ST** Prune stale abandoned local-only branches from origin (June 21–29 experiments) (OWNER, M) — ~40 origin branches are ahead of main with NO PR and last activity June 21–29 (agent/claude-, safety/, feat/, reliability/, sim/funded-test-account, etc.). They are stale experiments from the pre-worktree era, add noise to every branch scan, and confuse abandoned-work triage. Audit which are
- **ST** `Codex` Production-path RAG evaluator (worktree `/Users/jay/.codex/worktrees/rag-production-eval-20260721`, branch `codex/rag-production-eval-20260721`) — IN PROGRESS. Read-only corpus evaluator and DB case schema implemented; focused tests, scoped lint, and TypeScript green; committed locally and awaiting parent integration/PR. No provider/corpus/production mutation
- **ST** `Claude` BRANCH PROTECTION TEMPORARILY RELAXED to break a 34-PR merge deadlock
- **ST** `Antigravity` Watchlist & Order Row Button Tooltip Alignment — MERGED AS `07c2da3f` / AUTO-DEPLOY VERIFICATION PENDING. Aligned watchlist action button and order row action button tooltips to the right (`align="right"`) to prevent clipping at the screen's right edge. Passed verification gate (tsc, lint, test, build)
- **ST** `Codex` Admin authorization fail-closed hardening
- **ST** `Claude` Settings auto-save everywhere — ✅ COMPLETED
- **ST** `Claude` (6 rows, risk lane) — COMPLETED. Red-Team fail-open->policy-aware routing; vol-targeting sizing +
- **ST** `Claude` Durable pre-network stop-placement intent + atomic idempotent
- **ST** `Cursor` LLM cooldown + draining-account purge safety (PR #1845, branch `cursor/critical-bug-management-2b05`) — IN PROGRESS → landing. Code + rollout present; STATUS/EFFORT-LOG filled for handoff gate. Commit author identity: subsequent commits use noreply; squash-merge lands under PR merge identity
- **ST** `Claude` Tradier: broker-connection-only, no duplicate API-key Settings
- **ST** `Claude` Console radius + micro-type token sweep (branch `monet/console-token-sweep`
- **ST** `Claude` Settings de-iOS restoration + admin-link-in-chrome + site-wide UI expert review
- **ST** `Claude` `Codex` Bracket sibling-leg teardown: adversarial review follow-up + — P1 catch
- **ST** `Claude` Alpaca + Tradier bracket sibling-leg cancellation
- **ST** `Claude` Green/Red picker label coloring + Green Team/Red Team/Bull/Bear copy sweep
- **ST** `Claude` 2-3 day activity audit: find unresolved issues — COMPLETED
- **ST** Enrichment starvation: force-included scan candidates (holdings + event outliers) never
- **ST** `Claude` usage-cap pickup
- **ST** `Claude` Short stop-loss default (8%) + surface short settings in main Essentials
- **ST** `Claude` Model Stats drawer widened on desktop — COMPLETED
- **ST** `Claude` Scoring-factor weight tooltips — COMPLETED
- **ST** `Claude` Picker copy: "Proposer"/"Reviewer" + AI-review panel "Strategist"
- **ST** Settings affordance and tooltip pass - add clearer option descriptions/tooltips
- **ST** Universal ticker detail drawer parity - restore old-site discoverability by
- **ST** Intro landing fixes: viewport-true fallback box + eased retarget + fade gated on real
- **ST** `Claude` PRs #1019 / #1021 — RAG: server-side as-of Pinecone filter + persist-pool v2 (2 owner-approved
- **ST** `Claude` PRs #970 / #973 / #974 / #977 / #979 — next-wave RAG retrieval-quality + corpus-integrity
- **ST** `Antigravity` PR #844 - `claude/pr805-remediation`: P0 checkRegimeFlip RMW fix + P1 backlog + — connection-health
- **ST** `Claude` Global learning reads + batched advisory review of proposals ( cloud, branch
- **ST** `Claude` Per-team reasoning levels + rotation auto-effort + usage/Learning-Review links
- **ST** `Claude` PR #979 - Persist retrieved candidate pool for RAG analyzability
- **ST** `Claude` PR #1019 - Server-side point-in-time (as-of) filtering in Pinecone
- **ST** `Claude` PR #1021 - persist-pool-v2: pre-rankPool candidate pool + per-stage drop dispositions
- **ST** `Claude` PR #977 - Corpus-coverage receipt for requested-but-empty filings doc types
- **ST** PR #973 - RAG golden-eval expansion: episodic-analog cases + single-vs-multi-query (#822)
- **ST** `Claude` PR #970 - Typed retrieval-status receipt
- **ST** `Claude` PR #974 - Held-position retrieval scope
- **ST** PR #816 - Prompt-safety CR-H: fencing + deterministic injection receipts for the money-path
- **ST** PR #819 - Wire `usage-budget` Phase 2 (advisory-first, owner-overridable enforcement) into
- **ST** `Claude` PR #820 - Durable due-jobs substrate for 15m/1h intraday outcome sampling . Merged to
- **ST** `Claude` PR #822 - HyDE + evidence-derived multi-query retrieval for filings RAG, flag-gated
- **ST** `Codex` Coach chat -> framework primitives — ✅ COMPLETED via PR #810
- **ST** `Codex` Scan table column customization parity — ✅ COMPLETED via PR #806
- **ST** `Antigravity` Harden HMAC Security & Persistent Idempotency for webhooks — ✅ COMPLETED via PR #854. Updated `congress-webhook-auth.ts` to validate `X-Signature` header via HMAC SHA256. Created `processed_webhooks` db table and integrated persistent DB check in `markSeen` alongside in-memory cache to ensure persistent idempotency across server restarts. Lint and tests green
- **ST** `Claude` PRs #816 / #819 / #820 / #822 — planned-backlog train: prompt-safety fencing, usage-budget
- **ST** `Codex` PR #810 - Coach chat -> framework primitives . Merged to `main`
- **ST** `Codex` PR #806 - Scan table column customization parity . Merged to `main`
- **ST** `Claude` Pre-policy vetoes advisory-overridable — merged PR #814 (verify+smoke green)
- **ST** `Claude` Full-suite test determinism: de-flake order-confirmation-status + chat-orchestrator-search-knowledge — merged PR #812
- **ST** `Claude` Guardrails → overridable preferences (denylist) ( risk lane) — merged PR #799
- **ST** `Codex` PR #807 - Approvals triage upgrades + alert center . Merged to `main`
- **ST** `Claude` PR #694 - Effort-issues sync secondary-rate-limit hardening . Merged to `main`
- **ST** `Claude` PR #449 - Regime-enum adoption inside the risk gates ( risk lane). Merged to `main`
- **ST** `Claude` PR #374 - GitHub Issues mirror of the effort board , cross-app
- **ST** PR #350 - AI Review inheritance, model catalog, and text-box font controls
- **ST** PR #349 - Socratic admin/RAG/Pinecone/settings parity implementation
- **ST** PR #348 - Sell to Fund Buys title-case copy fix
- **ST** PR #347 - Console universe index exclusivity fix
- **ST** PR #346 - IRA wash-sale UI correction
- **ST** PR #345 - Run-state UX fix
- **ST** PR #344 - Socratic Trade Autonomy Desk implementation
- **ST** PR #340 - Socratic Trade rebrand
- **ST** `Antigravity` Fix mobile "Settings" crash inside Sheet — Fixed "Maximum call stack size exceeded" bug caused by a focus trap race condition when navigating to settings from the More sheet menu on mobile. PR pending
- **ST** `Antigravity` Harden HMAC Security & Persistent Idempotency for webhooks — moved back from Completed
- **ST** `Antigravity` Congress.Trade Improvements — Comprehensive improvements across UI, data sharing, and scraping. Worktree `~/apps/trading- `, branch `agent/antigravity`
- **ST** `Codex` Cloud Slack + effort-log readiness across all four apps
- **ST** `Cursor` ~~PR #808 — session: P0 checkRegimeFlip RMW fix + P1 backlog exhaustiveness ~~
- **ST** `Antigravity` ~~Admin connection health and backend-failure notification pass ~~
- **ST** `Cursor` `Claude` PR #856 - add — lane at port 4103, move — to 4104 (OWNER, S) — new row, IN PROGRESS
- **ST** `Claude` Shared-dep tokenless git-dependency switch — CLOSED, superseded by #444
- **ST** `Codex` global coordination + fleet monitoring setup
- **ST** `Claude` `claude/ci-hybrid-runner-verify`
- **ST** `Claude` `claude/drawdown-advisory-rescope` → PR #360, auto-merge armed
- **ST** `claude/w1-llm-fixes` — Bear schema confidenceScore fix (live bug); non-OpenAI reasoning-token headroom; cross-family Bear default + temperature; reward-abstention; stakes-scaled dissent trigger. STATUS: MERGED (PR #364)
- **CT** `Claude` Usage-compliance Wave 2 (CT lane): OpenRouter classifier metadata + generation-id capture (branch `claude/usage-compliance-ct`, worktree outside repo tree; — handoff pickup per `/Users/jay/apps/HANDOFF-usage-compliance-classifier- .md` + DESIGN-usage-compliance-classifier.md §2, incl. the RESOLVED flat-under-`trace` correction). Shared pin bumped v1.8.x
- **CT** `Codex` Backend delivery + ingestion reliability hardening — INTEGRATED +
- **CT** `Codex` Billing + platform security hardening — INTEGRATED LOCALLY + ADVERSARIALLY REVIEWED
- **CT** `Codex` iOS client correctness + performance hardening — INTEGRATED LOCALLY + REVIEWED
- **CT** `Claude` GPT-5.6 bake-off evaluation prep + usage/cost tracking harness — BUILT + PUSHED
- **CT** `Claude` Fix dead auto-publish gate: AGREEMENT_AUTOPUBLISH_MODEL_B was broken 2 weeks
- **CT** `Claude` Review-queue automation: model choice + multi-model consensus + escalation cascade
- **CT** `Codex` global coordination + fleet monitoring setup
- **CT** `Codex` Cloud Slack + effort-log readiness across all four apps
- **CT** Audit production schema drift from the three failed Deploy runs (OWNER, S) — Confirm whether
- **CT** `Claude` De-duplicate effort-issues sync when a row's first line changes
- **CT** Root cause of free-tier Class A pace ~162%: Litestream L0 PutObject per SQLite commit under `load_prices_st` bulk load
- **CT** (2) Loader: `analysis/massive-bulk-load/load_prices_st.py` + `load_prices.py` now batch with ` — commit-every 50` (fetch outside write lock; multi-ticker single commit). Host loader restarted root: `/tmp/load_prices_st.py — commit-every 50` state `/tmp/st_load_state.json`
- **CT** (3) Litestream: host `/etc/litestream/congress.yml` `sync-interval: 5m` (was 30s); service restarted; log shows `sync-interval=5m0s`
- **CT** (4) R2 cleanup on `congress-trade-bucket`: bulk/ kept last 3 dates only (−0.93 GiB), competitors/ deleted (−0.80 GiB), `_ops/usage-telemetry/` deleted (3759 objs). Tracked storage ~5.9 → ~3.8 GiB
- **CT** No app code/deploy required for this ops unit
- **CT** `Antigravity` `Gemini` OpenRouter Model Consolidation & Mistral OCR Integration — IN PROGRESS (PR #521 open, awaiting CI). Swapped direct model endpoints (OpenAI, , Anthropic, xAI) for their OpenRouter equivalents across default candidates, keeping native Mistral OCR as fallback. Updated settings validation to check underlying providers so multiple OpenRouter models can coexist in one lineup. Refac
- **CT** Live: `/api/health` costProfile paid; OpenRouter reads working (same row counts, field-level disagree remains on many legacy 2022 review docs). Autopublish enqueues 10+/tick. Review still ~1.9k (soft low_confidence + bad_asset_name + provider-gap)
- **CT** Live: `/api/health` costProfile paid; OpenRouter reads working (same row counts, field-level disagree remains on many legacy 2022 review docs). Autopublish enqueues 10+/tick. Review still ~1.9k (soft low_confidence + bad_asset_name + provider-gap)
- **CT** `Cursor` full reconcile (this chat + sister cloud `bc-df4b4649`): all GitHub Issues closed, boards synced. PR #898 fixed the effort-issues sync classifier (stops reopening finished rows). R2 proxy endpoint deployed via PR #912. Deno live ingestion parity handled. Owner-gated items (analytics, subscription login, R2 enablement, key ops, watcher-cron) resolved. Open GitHub issues went from
- **CT** `Codex` #714 P2 timestamp-sort follow-up — MERGED via #775 integration. Future-date clamp preserves full timestamp precision (dashboardHtml tests on main)
- **CT** `Codex` #749 Deno deploy PR conflict/comment closeout — SUPERSEDED / landed with Deno Deploy path
- **CT** `Codex` Deno live ingestion code path — MERGED PRs #754/#756/#757/#758/#760/#762/#764/#766/#769. Ops/parity follow-up remains in Active above
- **CT** `Antigravity` Time Filter Dropdown & Section Heading Styling — MERGED via #775. `#trGlobalWindow` on main
- **CT** `Claude` PR #649/555 deploy split — CLOSED (not merged); production deploy is `deploy-deno.yml`
- **CT** Deferred audit High/Medium (batchExtract Promise.all uploads, visionLlm chunking, PWA touch targets) — ALREADY ON MAIN (pMap concurrency 25; PR #541 massive-context skip; PR #419 a11y). Large `dashboardHtml.ts` → PWA migration remains a product program, not an open hotfix
- **CT** Deno Deploy & Turso Target: Integrated Deno server entrypoints (`src/deno/main.ts`), Deno Hono routing (`src/app.ts`), and Deno queue handlers (`src/queueHandlers.ts`). Updated `package.json` deploy script to use `deployctl` targeting Deno Deploy (`congress-trade`) and Turso database. Deprecated Cloudflare Workers / D1
- **CT** Top-Level Timeframe Filter: Added a single top-level Timeframe dropdown (`#trGlobalWindow`) to the Trends view toolbar, defaulting to Past 3 Months (`90d`). Styled section heading timeframes in italics (`<em class="tr-window-label">`)
- **CT** CI Runner Policy: Fixed `check-actions-runner-policy.mjs` error by updating `.github/workflows/auto-update-prs.yml` to target `[self-hosted, congress-ci]` and pinning action to commit SHA
- **CT** Fonts: Imported custom Zilla Slab font (Regular & Bold) into the Xcode project, registered in `.pbxproj` via `INFOPLIST_KEY_UIAppFonts`, and applied globally in SwiftUI via `App.swift`
- **CT** App Icon: Updated `AppIcon.appiconset` with the new custom logo resized to standard 1024x1024 resolution
- **CT** Portrait & Logo Porting: Integrated phase-based `AsyncImage` with party/chamber emoji fallbacks for profile pictures. Set up dynamic company logo fetches requesting light theme variants from the `/api/logos/ticker` endpoint, falling back to a monogram for non-ticker asset types (like House type codes)
- **CT** `Cursor` Executive Defaults & Cache Safety: Split `defaultChambers` from `initialChambers` so default UI selections include Executive disclosures while keeping backend default compatibility intact. Added `cacheHasExecutiveTrades()` checks on `cursorStore` to prevent mixed-cache sync — bugs
- **CT** Segmented Appearance Settings: Surfaced a segmented control in the Watchlist tab supporting "Match System", "Light", and "Dark" selections, updating the preferred color scheme at the application level
- **CT** Verification: Clean Xcode simulator build succeeded, and backend typecheck + full test suite passed
- **CT** PR 605 (SwiftUI Client): Clamped backoff delay to a max of 15 seconds in `CongressTradeStore.swift` to resolve UI freeze during 429 rate limiting. Squash-merged
- **CT** PR 607 (Ingestion Gaps): Integrated and merged to resolve ingestion discovery gaps
- **CT** PR 606 (Subscription Lifecycle): Implemented `POST /api/admin/subscriptions/:id/rotate-secret` (shown-once Bearer rotation) and `POST /api/admin/subscriptions/:id/deactivate` (frees slot from total quota, disables delivery). Updated SSE loop to query active status from D1 on each tick to terminate deactivated streams immediately. Resolved rebase conflicts in `migrations.ts` and `migrati
- **CT** `Antigravity` Deferred Audit Report Items — PLANNED/DEFERRED. The following items from the comprehensive audit report remain deferred for future work
- **CT** Backend: Refactor sequential uploads in `batchExtract.ts` to use `Promise.all()` (High); Re-evaluate PDF chunking in `visionLlm.ts` to leverage large context windows/caching (Medium); Implement robust JSON parsing instead of regex in `visionLlm.ts` and `bakeoff.ts` (Medium); Address memory pressure in `textPdf.ts` and string manipulation overhead in `consensus.ts` (Low)
- **CT** Frontend: Fix PWA mobile grid overflow and touch targets; migrate the 7,145-line `dashboardHtml.ts` logic to the modular Next.js PWA
- **CT** `Codex` Review Queue current drain + durable automation integration — DEPLOYED
- **CT** `Codex` Whole-app improvement roadmap implementation — IMPLEMENTATION COMPLETE LOCALLY +
- **CT** `Claude` `Codex` autofix: migrate CI loop from Anthropic to DeepSeek — DEPLOYED
- **CT** (record production Worker releases here after explicit owner-approved deploys)
- **CT** Follow-ups batch: brand archive + Zilla wordmark + exec filer enrichment + workerd diagnostics
- **CT** `Claude` Ingestion fetch outage: R2 known-length regression fix + dead-letter recovery
- **CT** `Claude` Executive-branch (Trump) trade tracking — OGE Form 278-T ingestion — BUILT
- **CT** `Claude` Public latency showcase + public delivery education + anti-scrape hardening
- **CT** `Claude` Shared-dep tokenless git-dependency switch . Both halves merged
- **CT** `Claude` PR #162 - Effort-issues sync secondary-rate-limit hardening . Merged to `main`
- **CT** (seeded empty — see repo git history for pre-protocol work)
- **CT** Web: delivery pause/resume/delete + filter editing (unassigned, M)
- **CT** Wave 4 go-live: configure auth + Stripe paywall services (unassigned, M) — board reservation
- **UM** `Grok` 2026-09-15 — IN PROGRESS — Land Usage-Monitor #1444 (boards `3482c85e` `ffcc1b58`, branch `claude/subscription-quota-pct`, worktree `~/apps/usage — sweep`). verify failed at branch coverage 69.68% < 70%. Adding tests for quota-windows, FleetQuotaMatrixCard, and subscription parsers. Threshold stays 70%
- **UM** `Grok` `Codex` `Claude` 2026-09-15 — COMPLETED — Land Usage-Monitor #1457 (board `53d391a7`, branch `codex/macos-keychain-prompts`, worktree `~/apps/usage — sweep-1457`). Merged origin/main. Kept — explicit Connect — path; dropped QuotaCore automatic Keychain reads. README keeps AgentBar pointer plus the Keychain-prompt docs
- **UM** `Codex` Infisical provider-credential auto-sync ( delegated implementation + security/runtime reviewers, owner-directed
- **UM** `Codex` Remaining-provider automatic enrichment implementation wave ( + provider teams
- **UM** `Antigravity` App-wide UI/UX Responsive and Accessibility Refinements — COMPLETED: Adding skeleton loaders, fixing table responsiveness on mobile, and semantic HTML fixes in ProviderCard. Merged implicitly into `main` via PR #66
- **UM** Bound generic usage-ingest request bodies before JSON decoding (unassigned, S) — MERGED PR #311 / DEPLOYED. OTLP ingest uses
- **UM** `Antigravity` Generic Service Cost Tracking & Project Schema Update — MERGED PR #66 / DEPLOYED. — COMPLETED: Decoupling API from Service in Provider, adding `Project` and `ProviderProjectAllocation` tables via Prisma to allow fractional cost attribution. (From architecture audit)
- **UM** `Claude` Fix /api/budget-status 401: exclude it from the dashboard-session middleware matcher — MERGED PR #58 / DEPLOYED
- **UM** `Antigravity` Resolve Agent Sync Relay noise and Anthropic must-keep-funded alerts — MERGED PR #113 / DEPLOYED. Updated `ensureAgentSyncProviderSeeded` to automatically disable the Agent Sync Relay provider on startup/poll, silencing the spurious missing_snapshot PagerDuty alerts. Also added a migration step in the same boot sequence to unflag `mustKeepFunded` for Anthropic since Anthropic does
- **UM** `Grok` Prod revision identity — LANDING. Deleted frozen Coolify `GIT_COMMIT_SHA`/`SOURCE_COMMIT` env; PR #1093 merged (prefer SOURCE_COMMIT); PR #1096 bakes SOURCE_COMMIT into image. Force rebuild after #1096 merges. Public may still show revision null until rebuild
- **UM** `Grok` Rename compose project oracle → usage-monitor — COMPLETED PR #1018 (`8f23199600fd`). Issue #1019 closed
- **UM** `Grok` iOS app icons clean orange + Local LOCAL stripe — COMPLETED PR #1009 (`750a28cede83`). Issue #1011 closed
- **UM** `Grok` R2 fleet ST/CT pushover-parity + iOS inline titles — COMPLETED PR #984 (`4be34c7e8815`). Issue #1006 closed
- **UM** `Grok` Fix auto-deploy race mid-build — COMPLETED PR #1001 (`61def229`). Issue #992 closed
- **UM** `Grok` Install replica-status probe + R2 kill reason — COMPLETED PR #989 (`098c9658c7b8`). Issue #990 closed
- **UM** `Grok` Issue/effort hygiene + replica age 3h — COMPLETED PR #976 (`6fc1def25ae8`). Issue #979 closed
- **UM** `Grok` Overview money UX — COMPLETED PR #949 (`146c9ca05b7b`). Issue #980 closed
- **UM** `Grok` iOS staleness banners + fetch coalescing + subscriptions read UI (P2, M) — PLANNED. Wire `BudgetStaleness`; single in-flight `BudgetStore` fetch; surface `APIClient.subscriptions()`
- **UM** `Grok` Producer retry-storm contract (ST/CT/OTLP wrappers) (P0, L, cross-repo) — PLANNED. Honor Retry-After; exponential backoff + circuit breaker; treat HTTP 202 as success regardless of `accepted`; never spin on `accepted: 0`. Cross-board rows on Socratic.Trade / Congress.Trade / shared as needed. Evidence: historical OOM→35rps overage
- **UM** `Grok` `Sentry` Dark-mode pass on Projects, Attention, , dashboard chrome (P1, S) — PLANNED. Complements residual dark-mode planned row
- **UM** `Grok` Cross-repo telemetry contract CI lock (P1, M) — PLANNED. Shared package vectors/enums vs `usage-telemetry.ts`; pin version. Cross: congress-trading-shared
- **UM** `Grok` Producer hard rules: always occurredAt ISO + explicit per-call idempotencyKey (P1, M, cross-repo) — PLANNED. Fix random-UUID when occurredAt missing; normalize ISO in basis only with coordinated bump
- **UM** `Grok` Optional verified-preferred cash mode for OpenRouter when coverage high (P2, L) — PLANNED. Audit layer today does not correct budgets
- **UM** Capture exact OpenAI, Mistral, and Google recurring subscription terms (unassigned, M). Current production has no local Subscription rows for these providers, and the integrated official usage/cost APIs do not expose the owner's consumer subscription purchase terms. Import an exact receipt or owner-supplied amount, currency, cadence, current-period start/end, renewal behavior, provider
- **UM** Implement OTLP logs ingestion (unassigned, L, deliberately deferred) — `/api/otlp/v1/logs`
- **CTS** Renamed remaining "Agentic Trading" references to "Socratic Trade" (PR #119)
- **CTS** Added Zod schemas for AmountBracket, Subscription, and SseMessage (PR #119)
- **CTS** Expanded client.ts and SseParser test coverage to 337 tests (PR #119)
- **CTS** Refined AmountBracketSchema to reject inverted bounds (PR #119)
- **CTS** Fixed TypeScript 6.0.3 and Zod v4 compatibility issues in tsup/schemas (PR #119)
- **CTS** Unified ticker normalizer regex & preferred/depositary helper functions (PR #97)
- **CTS** Relocated STOCK Act AmountBracket definitions & snapping/matching helpers (PR #97)
- **CTS** Aligned Zod schemas for ClientAsset and ClientTrade with production API outputs (PR #98)
- **CTS** Vitest CI test suite execution with strict code coverage minimum thresholds (PR #96)
- **CTS** Tokenless smoke-install verification job in CI (PR #96)
- **CTS** Corrected docs/RELEASE.md consumer notification list (PR #96)
- **CTS** CongressTradeClient + SUBSCRIPTIONS API path (PR #55)
- **CTS** balance/limit metricTypes (PR #56)
- **CTS** createCongressEvent helper and type dedup (PR #57)
- **CTS** Dependabot + weekly CI audit (PR #54)
- **CTS** (n/a for pre-1.3.0 — library package; "deployed" = version published/consumed by apps)
- **CTS** `Codex` Protect immutable release tags and enable repository-native security controls
- **CTS** `Claude` `Codex` autofix reusable workflow: migrate from Anthropic to DeepSeek
- **CTS** Make exact-pin drift checks tokenless, symmetric, and fail-closed (cross-app, P1/M)
- **CTS** `Antigravity` Split `TICKER_ALIASES` into rename-vs-acquisition classes — shared portion done in v1.3.0; consumer migration pending. ATVI→MSFT is
- **PS** `Antigravity` COMPLETED update ST and BotFleet app icons 2026-09-15
- **AR** `Antigravity` COMPLETED — GitHub Actions CI/CD for TestFlight Publish — · PR #192 merged. Set up `.github/workflows/testflight.yml` to securely codesign and publish the macOS and iOS apps to TestFlight via GitHub runners. Configured repo secrets. Triggered workflow dispatch
- **AR** `Antigravity` Web and iOS utility and power enhancements — · PR [#48](https://github.com/jaywedgeworth22/Autorotate/pull/48) (`ag/utility-power-enhancements`). Interactive .env importer & wizard, multi-select & batch actions, secret drift detection & live read-back inspector, dry-run simulator, workspace alert webhooks (Slack/Discord), QR pairing, Face ID biometrics, SwiftUI .env importer, QR scan
- **AR** `Grok` Merge — App Builder PWA with this monorepo — · merged as [#38](https://github.com/jaywedgeworth22/Autorotate/pull/38) (`900bd54`). Backups under `backups/`. Live web engine folds — rotators + parser + Mac agent
- **AR** `Cursor` `Grok` Apache-2.0 + Kimi dump backup + catalog fold-in — · PR [#42](https://github.com/jaywedgeworth22/Autorotate/pull/42) · branch `cursor/kimi-apache-merge`. Relicensed to Apache 2.0 (© Jay). Kimi dump at `backups/kimi-agent-autorotate/`. Secret Rotator nickname (`app/`) at `backups/secret-rotator/` (not a standalone app). — extra catalog folded into live web + AutorotateCore
- **AR** `Grok` `Antigravity` COMPLETED — Owner: Developer portal App IDs for Autorotate (Already Registered) — leftover after — #50 closed as duplicate of — #48. https://autorotate.codes. Do not reopen or merge #50. `com.jay.shellular` stays disabled
- **AR** `Cursor` COMPLETED/MERGED #178 — Dependabot leftover radix/react PRs — · after #16. Remaining npm PRs blocked on serial lockfile rebase. Auto-merge not enabled on the repo. PR #17 (`fix/no-target-commit`) is another seat — do not touch
- **AR** `Antigravity` COMPLETED — GitHub Actions CI/CD for TestFlight Publish — · PR #192 merged. Set up `.github/workflows/testflight.yml` to securely codesign and publish the macOS and iOS apps to TestFlight via GitHub runners. Configured repo secrets. Triggered workflow dispatch
- **CL** `Grok` Production host is Vercel at https://contactlogo.com (auto-deploy from `main`, `web/` as the project root). Coolify/Cloudflare are not the live host. — Publish at https://contact-logo.grok.me is legacy only
- **AFC** `Antigravity` `MiniMax` `Sentry` COMPLETED add — and — agents to fleet, update ST and BotFleet app icons in activity digest 2026-09-15
- **AFC** (n/a — machine-side infra is "deployed" when running under pm2/hooks; see Completed)
- **AFC** `Claude` Push pipeline RECEIVE path — BLOCKED on owner. Slack app Event Subscriptions not
- **AFC** `Codex` cloud Slack + effort-log readiness work (DONE-local, never pushed) — new row, IN PROGRESS
- **AFC** `Antigravity` Socratic.Trade PR #853 (effort-log mirror sync) still OPEN despite — 'DONE' claim — new row, IN
- **AFC** `Cursor` `Claude` Socratic.Trade PR #856 (port-lane docs: — 4103 / — 4104) still OPEN — new row, IN
- **AFC** `Antigravity` congress-trading-shared PRs #54/#55/#56 open despite — 'DONE' Slack claims — new row, IN
- **AFC** `Sentry` `Claude` `Antigravity` Congress.Trade PRs #181 ( CI reporter, ) and #182 (dep pin, ) open — new row, IN
- **AFC** `Claude` Effort-issues sync rate-limit hardening propagated fleet-wide ( + owner-spawned
- **AFC** Enable Slack Event Subscriptions so the relay receive path goes live (OWNER, S) — toggle +

## 2026-09-14

*0 PRs merged · 0 issues opened · 0 issues closed · 2 effort rows*

### Effort board

- **UM** `Claude` `Sentry` 2026-09-14 — COMPLETED (merged) - UM — ci-report hardening: committed harness in CI + guard tying MAX_RUNTIME_OVERRIDES to ios-ship.yml timeout-minutes. <! — wb-agent-report:3ccaa57e868e4878a0a5b68eca0cf35a — >
- **BF** `Antigravity` 2026-09-14 — COMPLETED - Fix desktop local updater exit 127 (Homebrew PATH) and iOS Live Activity main-thread hang (BOTFLEET-E). Landed in #414. Mac desktop exits 127 are fixed by injecting node paths. iOS Live Activity hang BOTFLEET-E fixed by shifting XPC call off MainActor. <! — wb-agent-report:ffc71298b94340ba856dda553b5ad090 — >

## 2026-09-13

*0 PRs merged · 0 issues opened · 0 issues closed · 57 effort rows*

### Effort board

- **CT** 2026-09-13 — FX — IN PROGRESS — Drop free/paid cost tiers; VACUUM INTO host backups; Stripe refund webhook; PDF 402 (`fx/aggressive-runtime-backups`, worktree `~/apps/congress-fx-runtime`, boards `d6226365` `cbed4f30` `93c48e00` `8932ea1f` `53548457`)
- **UM** `Codex` `Claude` 2026-09-13 — IN PROGRESS — Stop repeated — Keychain prompts in macOS monitor (board `53d391a7`, branch `codex/macos-keychain-prompts`, worktree `~/apps/usage-monitor — macos`). Existing — login remains intact. Automatic refreshes use file credentials or an in-memory credential snapshot; Keychain is reached only by explicit Settings actions. Issue #1455. All 51 native
- **UM** `Antigravity` `Sentry` 2026-09-13 — IN PROGRESS — Make — bug reporter subtle (autoInject false + nav trigger) (board `1cb294fd`, branch ` -subtle-feedback`, worktree `~/apps/usage — subtle`). Set `autoInject: false` in `src/instrumentation-client.ts` to eliminate floating button. Export safe `openSentryFeedback()` helper and wire subtle link into navigation Display and mobile drawer menus
- **UM** 2026-09-13 — FX — IN PROGRESS — USAGE_READ_TOKEN must not mutate alert routing (`fx/read-token-writes`, worktree `~/apps/usage-fx-read-token`, boards `154b622e` `e93a83fe`). Session-only PUT /api/settings. Same-repo pull_request auto-merge
- **UM** `Codex` `Grok` `Antigravity` 2026-09-13 — IN PROGRESS — Session telemetry completeness and collector reliability (branch `codex/telemetry-coverage`, worktree `/Users/jay/apps/usage — telemetry`, board `876172fe`). Live — collection reparses 27,964 events every 15 minutes and most recently ended on an ingest `internal_error`; — reparses 5,287. Installed jobs cover , , Copilot, and
- **UM** `Codex` `Antigravity` `MiniMax` `Grok` 2026-09-13 — COMPLETED - Native macOS Usage Monitor quota app (#1450, bfdd7e9a; issue #1449). Installed and verified menu bar/Dock/both with 49 Swift tests and green native/web/security CI. Four — shared windows, BotFleet marks, collapsed — video, hidden unused platforms, and live — Bot weekly allowance. Private quota-only BotFleet handoff is published; Bot
- **CTS** 2026-09-13 — FX — IN PROGRESS — Stop auto-merge on public-fork PRs (`fx/automerge-fork-guard`, worktree `~/apps/cts-fx-automerge`, boards `8bff5ca2` `417fe5e2`)
- **DD** 2026-09-13 — FX — IN PROGRESS — Skip pointless Vercel production deploys (`fx/vercel-skip-pointless`, worktree `~/apps/dealdex-fx-deploy`, board `0934111e`)
- **DD** 2026-09-13 — FX — IN PROGRESS — Merge to main is Vercel production (`fx/merge-equals-live`, worktree `~/apps/dealdex-fx-deploy`, board `ef71d6c1`)
- **DD** `Antigravity` `Sentry` 2026-09-13 — IN PROGRESS — Make — bug reporter subtle (autoInject false + footer/error trigger) (board `4c56f2de`, branch ` -subtle-feedback`, worktree `~/apps/dealdex — subtle`). Set `autoInject: false` in `src/lib/observability/sentry.ts` to eliminate floating button. Export `openSentryFeedback()` helper and add subtle trigger link to Shell footer and AppErr
- **AR** `Antigravity` `Sentry` 2026-09-13 — IN PROGRESS — Make — bug reporter subtle (autoInject false + footer/nav trigger) (board `87c80482`, branch ` -subtle-feedback`, worktree `~/apps/autorotate — subtle`). Set `autoInject: false` in `apps/web/src/lib/sentry.ts` to eliminate floating action button. Export `openSentryFeedback()` helper and wire subtle links into AppShell sidebar and lan
- **CL** `Antigravity` 2026-09-13 — COMPLETED — Phase 4: Multi-valued contact fields preservation and Google Contacts photo sync undo log (issues #72 & #75, PR #84 merged `e7c2d4c`). Preserve multi-valued emails, phones, and URLs across vCard, CSV, and Google import parsers; capture prior Google contact photos before overwrite with persistent undo log and UI restore action
- **CL** `Antigravity` 2026-09-13 — COMPLETED — Phase 3: First-party Vercel logo cache (/api/logo/:domain) integration in Swift & Android engines (issue #74, PR #82 merged `83e57a8`). Added ContactLogoCacheSource in Swift and contactLogoCache candidate in Android querying edge-cached 512px marks prior to fallback CDNs; bundled Vercel logo function to eliminate edge invocation failure
- **CL** `Antigravity` 2026-09-13 — COMPLETED — Phase 2: Full contact enumeration, personal contact guard, and opt-in affiliated review (issues #71 & #76, PR #80 merged `0cf8294`). Scans all 7,000+ address book entries; personal contacts protected from automatic badging; opt-in review tier for affiliated contacts (confidence capped at medium, unselected by default); scan breakdown counters and affiliate
- **CL** `Antigravity` 2026-09-13 — COMPLETED — Phase 1: Android batch query (issue #73) & Swift TaskGroup parallel matching for 7k+ scale (PR #78 merged `1aa54b4`). Batched Android `ContactsContract.Data` queries into a single projection query; bounded Swift `ReviewSession` matching via `withTaskGroup` (maxConcurrency = 8) with instant cancellation handling
- **AFC** 2026-09-13 — FX — IN PROGRESS — Skip pointless Vercel production deploys (`fx/vercel-skip-pointless`, worktree `~/apps/fleet-fx-deploy-docs`, board `0934111e`)
- **AFC** 2026-09-13 — FX — IN PROGRESS — Merge to main is Vercel production (`fx/merge-equals-live-docs`, worktree `~/apps/fleet-fx-deploy-docs`, board `ef71d6c1`)
- **AFC** 2026-09-13 — FX — IN PROGRESS — Register FX seat and HogHunter in fleet-apps.json (`fx/registry-fx-hoghunter`, worktree `~/apps/fleet-fx-registry`, board `22164b50`). FX row in Agent Seat table + Available (normal). HogHunter `HH` local-only. KIMI marked retired
- **BF** `Codex` 2026-09-13 — IN PROGRESS — Historical credential alert remediation (#390; board d24c7fd2). Isolated `~/apps/botfleet — build-exclusion-20260913` @ `codex/ios-build-exclusion-20260913` excludes Xcode build output. GitHub alerts remain open with validity unknown; credential replacement/revocation is separately outstanding. <! — build-exclusion-20260913 — >
- **BF** `Antigravity` `MiniMax` 2026-09-13 — IN_PROGRESS - Native computer tools for HTTP models and direct DSH — support. <! — wb-agent-report:5241e335df964cd0a3e785cdd3faa496 — >
- **BF** `Codex` 2026-09-13 — IN PR #402 — Local VM lifecycle and host Auto consent (issues #345, #346, #349; boards `7c2db2d7`, `1156a06d`, `1c63f177`; branch `codex/local-vm-safety-20260912`, worktree `~/apps/botfleet — vm-safety-20260912`). Bot deletion is fenced against VM mode changes; bulk and configuration-wide grants bind confirmation to exact displayed identities; per-bot Auto
- **BF** `Codex` 2026-09-13 — IN PR #404 — Native DeepSeek Harness ACP integration (issue #188; board `2784c3c7`; branch `codex/dsh-native-acp-20260912`, worktree `~/apps/botfleet — native-20260912`). The driver uses the published `dsh — profile acp` transport with standard MCP, native resume, verified opaque model/reasoning selection, strict stock-version readiness, cancellation-safe pr
- **BF** `Codex` 2026-09-13 — IN PR #348 — Make routine calendar timezones explicit (issue #337; board `d308d7a8`; branch `codex/calendar-timezone-20260912`, worktree `~/apps/botfleet — timezone-20260912`). Calendar placement, date headers, inputs, and run labels use the selected effective zone; explicit recurrence zones survive scheduler and package round trips, while legacy schedu
- **BF** `Codex` 2026-09-13 — IN_PROGRESS - Durable BotFleet usage telemetry outbox. <! — wb-agent-report:82ab4e6dbdf142dabdbc159cee29eb99 — >
- **BF** `Codex` 2026-09-13 — IN PROGRESS — model catalog refresh (#391, PR #393). Current CLI catalog remains authoritative; the fallback offers current coding models and preserves stored retired or provider-qualified selections, including implicit OpenAI configs. Fourteen catalog regressions pass; complete canonical hosted CI is required before merge. <! — wb-agent-report:7326161cab684
- **BF** `Codex` 2026-09-13 — IN PROGRESS — Historical credential alert remediation (#390; board d24c7fd2). Isolated `~/apps/botfleet — build-exclusion-20260913` @ `codex/ios-build-exclusion-20260913` excludes Xcode build output. GitHub alerts remain open with validity unknown; credential replacement/revocation is separately outstanding. <! — build-exclusion-20260913 — >
- **BF** `Claude` `MiniMax` 2026-09-13 — IN_PROGRESS - Quota parity: — balance and cap status, window mapping for six engines, dual-window labels for every engine (parity G11+G12+G13). <! — wb-agent-report:a72269bdfec84418a6fd2405035c75cc — >
- **BF** `Claude` `MiniMax` 2026-09-13 — IN_PROGRESS — connectability: vault and config.json key sourcing, encrypted store, second instance from the app (parity G3+G6). <! — wb-agent-report:f59883b6952e45c2b703fe6e2133b81b — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Push hardening: time-sensitive kinds, retries, cached provider token, sender health, lock-screen Approve/Deny. <! — wb-agent-report:761055f9973348a9b94369c207bb9512 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - iOS: Mac Update card with remote install, and a newer-TestFlight-build notice. <! — wb-agent-report:5d5d55b75e404a688ebef504af0d6a28 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Check and install Mac updates from the app and the phone: harness /api/update routes, detached launcher, desktop UI. <! — wb-agent-report:baf4f722e2944d568adffeb41b23feb7 — >
- **BF** `Claude` `MiniMax` 2026-09-13 — IN_PROGRESS — connectability: vault and config.json key sourcing, encrypted store, second instance from the app (parity G3+G6). <! — wb-agent-report:f59883b6952e45c2b703fe6e2133b81b — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Remove stray tracked root scripts and the OpenMausBot mascot preview page. <! — wb-agent-report:a1a56bdb06e34c329a983d3bdd7f8a32 — >
- **BF** `Codex` 2026-09-13 — IN PROGRESS — Board reconciliation acceptance (#286; board 66958de4). PR #350 merged as `dff6af37` after every required check passed, adding the audit report/parser corrections and complete hosted test chain. Historical metadata corrections preserve peer ownership; broader current-state audit and deployed-versus-merged reconciliation remain open. Worktree `~/apps
- **BF** `Codex` `Claude` `Sentry` `MiniMax` 2026-09-13 — IN PROGRESS — OpenAI-compatible tool loop (#355, PR #403), handed over from — PR3. Shared approval-aware loop replaces the legacy executor. Streamed usage survives failure in terminal events and — chat spans; optional usage requests retry once only for explicit unsupported-field errors; canonical tool events avoid duplicate spans. 123 focused driver
- **BF** `Codex` 2026-09-13 — IN PROGRESS — Streaming reply visibility and reconnect recovery (#353, PR #397). Active code renders without invoking highlighting; completion invokes it once. Real StoreProvider browser checks prove resumable streams survive, non-resumable gaps clear text/reasoning and buffered deltas, and the next turn starts clean. Forty-eight store tests pass; current full hos
- **BF** `Codex` 2026-09-13 — IN PROGRESS — Composio connected-account readiness (#270, PR #398). Typed credential/transport/upstream status, retained same-identity last-success evidence, scoped-key 403 fallback, and identical-credential reconnect preservation. Twenty-four server regressions pass; browser screenshot recorded; complete canonical hosted CI and live acceptance remain pending. Wor
- **BF** `Antigravity` 2026-09-13 — IN PR #354 — Action chips draft population, bot profile sheet cancellation guard & model cache, turn replay byte cap, honest tool-support copy (board `77582325`; branch `ag/audit-fixes`, worktree `~/apps/botfleet — audit-fixes`). Populate composer draft from predictive action chips instead of immediate dispatch to prevent accidental runs; rethrow Swift Concurrency Can
- **BF** `Claude` `MiniMax` 2026-09-13 — IN_PROGRESS - Quota parity: — balance and cap status, window mapping for six engines, dual-window labels for every engine (parity G11+G12+G13). <! — wb-agent-report:a72269bdfec84418a6fd2405035c75cc — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - iOS: Mac Update card with remote install, and a newer-TestFlight-build notice. <! — wb-agent-report:5d5d55b75e404a688ebef504af0d6a28 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Push hardening: time-sensitive kinds, retries, cached provider token, sender health, lock-screen Approve/Deny. <! — wb-agent-report:761055f9973348a9b94369c207bb9512 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Check and install Mac updates from the app and the phone: harness /api/update routes, detached launcher, desktop UI. <! — wb-agent-report:baf4f722e2944d568adffeb41b23feb7 — >
- **BF** `Codex` 2026-09-13 — COMPLETED (PR #405 merged `18448f9c`) — Correct DeepSeek API rates and billing-window display (#396; board `beb8234081e546fd846143581e111226`). DeepSeek V4.1 Flash and V4 Pro now show official off-peak–peak input, cache-read, and output ranges with UTC windows and dated source copy; API reference estimates remain separate from provider charges and subscription limi
- **BF** `Antigravity` `Sentry` 2026-09-13 — IN_PROGRESS - Fix chat bottom scroll with attachments and move — bug report off send button. <! — wb-agent-report:df0a3beec1b642d7979394c4e96b6cd6 — >
- **BF** `Codex` 2026-09-13 — COMPLETED (PR #356 merged) — Prevent successful replies from triggering quota cooldown/fallback (issue #351; board `79fa2368`; branch `codex/quota-classifier-evidence-20260912`, worktree `~/apps/botfleet — classifier-20260912`). Quota fallback now requires structured provider evidence or a strict terminal chip; ordinary success prose about subscription, t
- **BF** `Codex` `Sentry` 2026-09-13 — COMPLETED (PR #352 merged) — diagnostics reliability (issues #341–#343; boards `13008da2`, `c5217e2b`, `a0794219`; branch ` -diagnostics-reliability-20260912`, worktree `~/apps/botfleet — diagnostics-20260912`). The packaged renderer waits for the saved diagnostics switch before starting , clearing the visible environment restores
- **BF** `Claude` `MiniMax` 2026-09-13 — IN_PROGRESS - Provider parity audit ( first tier; matrix across functionality, telemetry, quota/subscription, autonomy, connectability) — read-only, feeds lanes. <! — wb-agent-report:2ca7e5db51c5417289cb2c7f0cf72959 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - APNs and Live Activities audit: end-to-end push wiring, LA lifecycle, BOTFLEET-E hang, better uses. <! — wb-agent-report:c871445c9268425c85a91dc4ccd8416c — >
- **BF** `Claude` 2026-09-13 — COMPLETED - Bot roles brainstorm note for the owner: current roster, tuned variants, alternative role cuts, alternative bot definitions. Note published: [BF, ] Bot roles brainstorm. <! — wb-agent-report:c9d5b0cb9ae44b43bc6040cd84135abd — >
- **BF** `Antigravity` 2026-09-13 — IN_PROGRESS - Dual-window quota display (5hr/Week), DeepSeek balance and rolling spend. <! — wb-agent-report:137f0c87ef8a4cd085edf126a7f9e824 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Mac updater hardening after post-merge review of #371: stamped stage rollback path, vnode-based survivor detection, bundle-internal daemons, orphan and installing-receipt reconciliation. <! — wb-agent-report:7e929296f5104175a2cd6f23f13ad158 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Bound native/events transcript growth under ~/.botfleet (1.9 GB per-thread ndjson files). <! — wb-agent-report:71499ed63b5d48599e1ebb60edfffe92 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Tests leave orphaned harness node children (26 GB resident) — process-group kill on teardown. <! — wb-agent-report:acfc0c9f197e4629abb2473611bad0d1 — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Boot error page: text only, Try Again relaunch link (owner request after #359). <! — wb-agent-report:f95739cb34784d399347a92a44412bce — >
- **BF** `Claude` 2026-09-13 — IN_PROGRESS - Mac updater: keep rollback bundles out of /Applications, prune after verification, no rollback-named running app. <! — wb-agent-report:859bcdf085524ba99ee1e54bfbdb27ae — >
- **BF** `Claude` `Sentry` 2026-09-13 — IN_PROGRESS — driver passes — permission-prompt-tool mcp__ogb__approve without the proxy registered ( BOTFLEET-8). <! — wb-agent-report:014bfe35001347df841d1df798da494f — >
- **BF** `Claude` 2026-09-13 — COMPLETED - Per-thread transcript ndjson logs grow without bound (1.9 GB on the owner's Mac). Duplicate of 71499ed6; PR #373 tracked there. <! — wb-agent-report:cf8a05167ee44f74b8dd864f1ffe3e15 — >

## 2026-09-12

*0 PRs merged · 0 issues opened · 0 issues closed · 19 effort rows*

### Effort board

- **CT** `Antigravity` 2026-09-12 — COMPLETED — Full-stack codebase & operations audit, comprehensive issues log & remediation plan (branch `antigravity/full-stack-audit-2026-09`, issues #2364, #2365, #2366, #2367, #2368). Conducted deep multi-agent review across backend architecture, ingestion pipeline, web UI/UX, iOS client, and database/storage ops with live production probes (HEAD SHA `7f36e3b2`). Logged
- **UM** `Antigravity` 2026-09-12 — IN PROGRESS — Resolve all open app issues across GitHub issues, effort log, and Mac board (branch antigravity/resolve-all-app-issues). Fix collectors token resolution to ~/.secrets/global-api-keys and launchd plists; land PagerDuty #79/#105/#104 fix; reconcile effort logs and sync GitHub issues
- **CL** `Antigravity` 2026-09-12 — COMPLETED — Thorough app review, audit issues #71–#76, and contact scan drop analysis (PR #77 merged `a059193`). Diagnosed contact enumeration and classification drop in `CNContactsProvider` and `ReviewSession`; filed GitHub issues #71–#76; documented in `docs/audit/2026-09-12-full-app-audit.md`; updated `AGENTS.md` and Apple Notes
- **BF** `Codex` 2026-09-12 — IN PROGRESS — Throttle highlighting during streamed replies (#353; board 001dfbb5). Owned worktree `~/apps/botfleet — highlight-20260912` @ `codex/streaming-highlight-20260912`. Restore the hidden live reply bubble and pass the existing streaming flag to ChatMarkdown; preserve immediate highlighting after completion. Browser inspection reproduced the
- **BF** `Codex` 2026-09-12 — IN PROGRESS — Fleet RAG routing and readiness (#271/#272, boards 2d627f55 / 432930fc). PR #327 merged at `3a02f23a` with full green CI; #272 completed. Renderer route/freshness display is in #330, and deployed acceptance remains open under #271. Fleet recall lesson stored as `contrib/CODEX/2026-09-12/8a631b87`. <! — readiness-20260912 — >
- **BF** `Codex` 2026-09-12 — IN_PROGRESS - [P1] Require Auto consent for inherited host computer grants. <! — wb-agent-report:1c63f177953c4b939a5a6095a62beb61 — >
- **BF** `Codex` 2026-09-12 — IN PROGRESS — Complete signed macOS update feed and release automation (#285; board `5a2b2e02bf5c4debbc0559d2009032d0`; branch `codex/release-linux-feed-20260912`, worktree `/Users/jay/apps/botfleet — feed-20260912`). PR #334 is merged; hosted run 34686539553 attempt 2 passes dual-architecture signing, notarization, and stapling. Fixing the assembly ver
- **BF** 2026-09-12 — BF-DESIGNER — IN PROGRESS — iOS roster keeps Bot Chats separate from user rooms (board `bf86a7bf`, branch `grok/ios-bot-chats`, worktree `~/apps/botfleet-designer-ios-bot-chats`). `group.dm` rooms leave the Channels/Rooms section and sit in Bot Chats at the bottom, default collapsed, matching Mac. Extra-ship no. No TestFlight. <! — wb-agent-report:bf86a7bff1e345dda62ab68
- **BF** `Codex` 2026-09-12 — IN PROGRESS — Authenticated build/API identity and Mac update acceptance (#265/#274, boards e4190ce1 / 7e582b82). Signed app and detached harness/dependencies installed at `ae8abe7d`; authenticated PID 11581, one SQLite owner, loaded desktop and unsent draft verified. Newer fixes and full engine/iPhone acceptance remain pending; prior rollback copies retained. <!
- **BF** `Grok` `Codex` 2026-09-12 — COMPLETED - Map Remote Access Test Connection pill to product copy. Implemented by — in #308 (7d5a7cd8f9c03e1da93ff0771f1d9460fd99b605). — #286 reconciliation verified Reachable / Could not reach / timeout mapping and matching Test Connection accessible name in current source. No new runtime deployment claimed. <! — wb-agent-report:f3c03a1060cd4be1b21c83b0b
- **BF** `Codex` 2026-09-12 — COMPLETED — Routine outcome reliability (#284, board c0f364ea). Worktree `~/apps/botfleet — outcomes-20260912` @ `codex/routine-outcomes-20260912`. Combined receipts now retain and share actual execution outcomes; safe causes/phases, actual engine identity, and per-routine seven-day metrics distinguish cancellation/denial from failure. Typecheck, 54 f
- **BF** `Codex` 2026-09-12 — COMPLETED — Credential restoration and authenticated alert delivery (#269/#270/#273/#329, PR #333). Merged as `cdba649d`. Durable nonsecret presence markers and authenticated replay gate only consumers of missing encrypted credentials; interactive, room, fallback, boot-recovery, and routine work resumes once without exposing keys. Candidate credential preparation
- **BF** `Codex` 2026-09-12 — COMPLETED - Replay encrypted workspace credentials when desktop attaches to the always-on harness. Landed in PR #333 at `cdba649d`; signed live credential acceptance remains under #274. <! — wb-agent-report:eebedc2e674b442d99ae3e71aff1eccd — >
- **BF** `Codex` 2026-09-12 — PLANNED - [P2] Unify routine calendar and outcome timezones. <! — wb-agent-report:d308d7a8ecee443490e6bd7a4561ca46 — >
- **BF** `Codex` 2026-09-12 — PLANNED - [P2] Preserve active routine receipt groups during history pruning. <! — wb-agent-report:f34fe9d7fece46bba54d7d6fe77b3497 — >
- **BF** `Codex` 2026-09-12 — COMPLETED — Preserve active routine receipt groups (#336, PR #347; board f34fe9d7). Merged as `6bc0ac68` with all seven hosted CI jobs green. Active groups and unsettled confirmation results survive the 2,000-record terminal tail; durable reload/retry behavior passed peer review and the full local gate (3,588 Vitest tests, 19 skipped, all chained suites). Signed
- **BF** `Codex` 2026-09-12 — IN_PROGRESS - Remove stale one-off root patch scripts and compiled artifact (#320). <! — wb-agent-report:e24dac98660b49078c01ec98d5e621de — >
- **BF** `Codex` `Cursor` 2026-09-12 — COMPLETED — Engine resume, deadline, and VPS lease safety (PR #324; merge `c9807099`; issues #280, #281, #321; boards `89a63172`, `689d0f4e`, `6ca81ed5`; branch `codex/engine-resilience-20260912`, worktree `~/apps/botfleet — resilience-20260912`). ACP and — now preserve the saved — instead of silently starting an empty session; — retries tra
- **BF** `Codex` `Antigravity` 2026-09-12 — COMPLETED — Correct — quota routing (#283, PR #338, board 09d689cb). Merged as `abe978c6`. Maps live opaque model labels to exact catalog identities, preserves conservative reset bounds, and clears recovered aliases. Full gate passed 3,554 Vitest tests plus chained suites; 84 focused tests passed after peer corrections. Installed Mac acceptance remains

## 2026-09-11

*0 PRs merged · 0 issues opened · 0 issues closed · 16 effort rows*

### Effort board

- **BF** `Codex` 2026-09-11 — PLANNED - Reduce full CI runs for documentation-only changes. <! — wb-agent-report:34813b74e32a4b57b2687ff255f9bcfe — >
- **BF** `Codex` 2026-09-11 — PLANNED - Make local BotFleet updates preserve active work and support rollback. <! — wb-agent-report:e296144327fc4cdab5960e6cff0f7ae5 — >
- **BF** `Codex` 2026-09-11 — PLANNED - [P2] iOS cannot interrupt a busy room. <! — wb-agent-report:4bb6be1026dd4b109d945e4ca59c78bb — >
- **BF** 2026-09-11 - BF-COMPILER - PLANNED - BotFleet main CI red: package + smoke (Ubuntu) — packaged-app SIGTERM lifecycle smoke, Electron exited 127. <! — wb-agent-report:134116982972424e8a22de3bc9a76e58 — >
- **BF** `Codex` 2026-09-11 — COMPLETED — [P1] Patch vulnerable Next and image dependencies in the docs workspace (issue #311, PR #316, board `b9102d9e2b4a498183a0808556791fdd`). Next.js 16.3.3 and Sharp 0.35.4 are locked; hosted docs type generation and production build passed. Landed as `7ae5c8c1`; no deployment or restart was performed. <! — wb-agent-report:b9102d9e2b4a498183a0808556791fdd
- **BF** `Codex` 2026-09-11 — COMPLETED — Remediate vulnerable Electron packaging dependencies and verify generated artifacts (issue #296, PR #316, board `2c27a6351b18472993007b0a9f86d24d`). Electron Builder 26.16.1 passed hosted Linux AppImage/DEB, native Windows NSIS, and unsigned macOS arm64 packaging checks. Landed as `7ae5c8c1`; native package evidence is from unchanged packaging inputs a
- **BF** `Codex` `Grok` 2026-09-11 — COMPLETED — Provider request isolation (#278/#279, PR #314, boards `5344a9835c2648b5b96cb58bec81f122` / `93839dda22d84857932b4bebff31f01c`). Landed as `86410c70` with green final hosted CI. Strict MCP configuration covers bot turns and tool-free title/review helpers; cached capability checks guard launches; — history is constructed once. Full local gate passed
- **BF** `Codex` 2026-09-11 — COMPLETED — iOS task-bound Send/Stop, idempotent retry, and background APNs safety (boards `39f7be5c`, `18341d8c`, `118caef5`, `4505f828`; issues #287–#290). Landed in PR #312 as `cf51b991`. Actions now bind to the displayed thread, lost-response retries reuse one idempotency key, stale committed sends replay safely, and background APNs refreshes without navigatio
- **BF** `Antigravity` 2026-09-11 — COMPLETED - [P1] Infisical timeout handling and full write-through sync. Landed in PR #309 (squash 2246f19e) on BotFleet and deployed via update-botfleet.sh. <! — wb-agent-report:42937fa4ac3f40f79c29c7569dae7a1a — >
- **BF** `Antigravity` 2026-09-11 — COMPLETED - Scope PATCH /api/instances to affected engine and fix settings lock stall. Landed in PR #297 on BotFleet <! — wb-agent-report:2256455865414dd2bf90096f23dbf725 — >
- **BF** `Antigravity` `MiniMax` `Codex` 2026-09-11 — COMPLETED / DEPLOYED — Quota telemetry countdowns, rates table cleanup, — & Custom Engines in Settings, DeepSeek & — logo adjustments (PR #303 squash `2303ec3c`, board `3271270141be46768817d261e11df9d8`, branch `ag/quota-rates-custom-engines`). Merged to main and deployed to local /Applications/BotFleet.app and LaunchAgent com.jay.botfleet-server via update
- **BF** `Grok` 2026-09-11 — COMPLETED / DEPLOYED — Map Remote Access Test Connection pill to product copy (PR #308, board `f3c03a10`, branch `grok/remote-access-test-copy`). Merged to main and deployed via update-botfleet.sh
- **BF** `Grok` 2026-09-11 — IN PROGRESS — Map Remote Access Test Connection pill to product copy (board `f3c03a10`, branch `grok/remote-access-test-copy`, worktree `~/apps/botfleet-designer-remote-access-copy`). Designer follow-up to #298. Extra-ship no. <! — wb-agent-report:f3c03a1060cd4be1b21c83b0b4ef4e67 — >
- **BF** 2026-09-11 - BF-DIRECTOR - COMPLETED - Settings Remote Access test button and Infisical sync verification. Landed: BotFleet PR #298 merged 2026-09-11 01:06Z (e60f68a6). <! — wb-agent-report:9a4266a573f140e8890d3a0be16b6f60 — >
- **BF** 2026-09-11 - BF-DIRECTOR - COMPLETED - UI pass: system-instruction card chrome on PR #299. Landed: BotFleet PR #301 merged 2026-09-11 00:29Z (566f398e). <! — wb-agent-report:1476cdc17ee047a3be906615a5da0e83 — >
- **BF** 2026-09-11 - BF-DIRECTOR - COMPLETED - Same-source/routine re-fires must append; auto instructions not user bubbles. Landed: BotFleet PR #299 merged 2026-09-11 00:13Z (6c395ebd). <! — wb-agent-report:3d9ff839fbe6437e8ca6b22ddee351d1 — >

## 2026-09-10

*0 PRs merged · 0 issues opened · 0 issues closed · 3 effort rows*

### Effort board

- **BF** `Claude` 2026-09-10 — IN_PROGRESS - Redaction wrapper scan: a prose quote opens a false wrapper, an escaped wrapper is missed, a short credential after a scheme is unmasked. <! — wb-agent-report:3f57540fc5e6470cb70f57f6592e792b — >
- **BF** 2026-09-11 - BF-DIRECTOR - COMPLETED - BOTFLEET-C grokAgent auth_required while signed in. Landed: BotFleet PR #304 merged 2026-09-10 21:08Z (787a814d). <! — wb-agent-report:e86443a4cc2043df90834fafb7caa6ba — >
- **BF** `Claude` 2026-09-10 — COMPLETED - Redaction auth-header pattern leaks a long OAuth parameter and eats JSON siblings. Landed in #306 (09cc49f6). <! — wb-agent-report:d7b670383f7f4d4e978890d9df8a0032 — >

## 2026-09-09

*0 PRs merged · 0 issues opened · 0 issues closed · 16 effort rows*

### Effort board

- **CT** `Claude` `Codex` 2026-09-09 — COMPLETED/DEPLOYED #2356 (`92da50d9`) — Hotfix: hide the Trades search on the Trends tab for phones / coarse-pointer tablets ( P2 on #2353) (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). The #2353 review-fix rule `#ctFilters #tradesExtraFilters { display:flex }` (phone block, specificity 2,0,0) outranked `html[data-view="trends"] #tradesExtraF
- **CT** `Claude` 2026-09-09 — COMPLETED/DEPLOYED #2353 (`03770ac2`) — Header chrome rework: filters right of the logo (shared Trades/Trends row), one control radius, admin-gated tabs, ST-style sign-in buttons, single-row phone pager band (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). Owner: filters should sit right of the logo with the same corner radius as the section tabs, ca
- **CT** `Claude` 2026-09-09 — COMPLETED/DEPLOYED #2350 (`c4474f2d`) — Trades "Buy" pill ink white on light mode (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). Owner: "Buy should be white inside the green pill since can't read it like at all so then it'll look like the red Sell pills do". `.tag.B, .tag.P` carried near-black ink (`#080c17`) chosen for dark mode's bright `#22c55e
- **PS** `Antigravity` 2026-09-09 — IN PROGRESS — Add Vercel Speed Insights to Personal-Site (branch `ag/speed-insights`, worktree `~/apps/personal- `). Added `@vercel/speed-insights/react` component to `__root.tsx` alongside existing `@vercel/analytics`
- **BF** `Claude` 2026-09-09 — PLANNED - Fleet acknowledgement dialog hides which/how many bots get Auto host control. <! — wb-agent-report:1156a06d643f4b39a2a32c47928f84ef — >
- **BF** `Claude` 2026-09-09 — PLANNED - VM mode switch races with bot DELETE - no fence, partial cleanup errors. <! — wb-agent-report:7c2db2d7b9de489ea3d300f673b77d60 — >
- **BF** `Claude` 2026-09-09 — PLANNED - observability-config.ts: clearing environment field does not clear stored value. <! — wb-agent-report:c5217e2bf42f432a8c89c62045c30725 — >
- **BF** `Claude` `Sentry` 2026-09-09 — PLANNED — ai.ts: one failed turn reports two — exceptions. <! — wb-agent-report:a079421914ab4a73b15cabc98e2f3582 — >
- **BF** `Antigravity` 2026-09-09 — COMPLETED / DEPLOYED — Scope PATCH /api/instances to affected engine and fix settings lock stall (PR #297, board `22564558`, branch `ag/scoped-engine-reload`). Merged to main and deployed
- **BF** `Antigravity` 2026-09-09 — IN PROGRESS — Bot ↔ Bot heading parity and iOS settings save resilience (board `f16194b9`, `9a9f4cef`, branch `ag/bot-to-bot-heading`, worktree `~/apps/botfleet — bot-heading`). Rename Bot Chats to Bot ↔ Bot on Mac and iOS; add Bot ↔ Bot collapsible section to iOS ChatListView; fix iOS AgentProfileView and GroupProfileView sheet dismissal on failed save
- **BF** `Antigravity` `MiniMax` `Codex` 2026-09-09 — IN PROGRESS — Quota telemetry countdowns, rates table cleanup, — & Custom Engines in Settings, DeepSeek & — logo adjustments (board `3271270141be46768817d261e11df9d8`, branch `ag/quota-rates-custom-engines`, worktree `~/apps/botfleet — quota-engines`). Strip static CLI rows from pricing table; remove redundant lower Usage Monitor breakdown; add explicit 5h
- **BF** `Sentry` 2026-09-09 - BF-FIXER - IN_PROGRESS - BOTFLEET-C grokAgent auth_required while signed in. Board `e86443a4`. Branch `fixer/auth-required-ambient`, worktree `~/apps/botfleet-fixer-auth-required`. ACP fail-closed only when auth.json is missing; — skips setup/cancel Issues. No TestFlight
- **BF** `Antigravity` `Cursor` 2026-09-09 — IN_PROGRESS - Scope PATCH /api/instances to affected engine and fix settings lock stall. Board 22564558. Branch ag/scoped-engine-reload, worktree ~/apps/botfleet — engine-settings. Scope instance reload and describe to the modified provider; add TTL caching to — CLI models/auth; lift EnginesSettings UI busy state and update store directly to prevent 409 collis
- **BF** `Claude` `Sentry` 2026-09-09 — PLANNED — ai.ts: failed tool result detail sent to — unredacted. <! — wb-agent-report:a5688de705dd4413bfdd9e0c107d9f6b — >
- **BF** `Claude` `MiniMax` 2026-09-09 — IN PR #357 — PR 10/11: typed HTTP errors, honest — snapshot, — on the failover ladder (board `83e9a706`, branch ` -10-typed-errors-snapshot-ladder`, worktree `~/apps/botfleet — 10`, parent `cdba649d`). New `server/drivers/chat-completions/errors.ts` maps an HTTP status onto the shared `ProviderErrorCode` union the ACP drivers already
- **BF** `Codex` 2026-09-09 — COMPLETED — End-to-end iOS, macOS, engines and integrations audit (PR #295, board `55bff4ee`, issue #263). Completion record for this documentation merge: 35 findings, 32 new follow-up issues plus expanded #93/#188, 35 canonical Mac board items, report and structured ledger under `docs/audits/2026-09-09-`. Full pnpm gate and 234 Swift core tests passed; local uns

## 2026-09-08

*0 PRs merged · 0 issues opened · 0 issues closed · 42 effort rows*

### Effort board

- **CT** `Claude` 2026-09-08 — COMPLETED/DEPLOYED #2348 (`2700718a`) — Trends "Committee Sector Conflicts" table: names + committees first, rest on hover / row click (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). Owner: politician names must be readable, show as much committee info as fits and the rest on mouseover or by clicking the row into the politician's drawer, then size t
- **CT** `Claude` 2026-09-08 — COMPLETED/DEPLOYED #2346 (`bb5b0b43`) — Trends chrome follow-up from the owner's iPhone screenshot (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). Owner: the filter strip sits under the logo, so the nav cannot be centered on the combined band — reverted the ` — ct-filter-h`/2 offset, nav + account center on the header row only; wordmark larger on pho
- **CT** `Claude` 2026-09-08 — COMPLETED/DEPLOYED #2344 (`792ee581`) — Web chrome on the content column + Trends flow-row polish (branch `claude/congress-trade-trends-layout-b712w3`, cloud session). Owner screenshots: header wordmark, nav and the sticky filter chips sat at a 35px viewport inset while the Trends cards start at the 1280px column (320px in at 1920), nav sat high in the white band, and th
- **CT** `Grok` 2026-09-08 — IN PR — Deterministic agreement autopublish: cheap-first, budget-stop, reuse quality extracts, junk-gate, LlamaParse off the OpenRouter per-doc USD latch (board `a1f4ff1e`, branch `grok/agree-reuse-budget-stop`). H-2026-9116328 spent ~$0.34; luna 242 good; haiku junk; LlamaParse blocked by 0.25. Cascade runs cheapest first and stops remaining USD-metered OR calls before a
- **CT** `Grok` 2026-09-08 — IN PR — Deterministic agreement autopublish: cheap-first, budget-stop, reuse good extracts, quality-gate junk (board `a1f4ff1e`, branch `grok/agree-reuse-budget-stop`). H-2026-9116328 was hand-published 242 txs from gpt-5.6-luna after haiku junk and a later batch dying on the 0.25 per-doc ceiling left the good extract unused. Cache reuse now runs before the per-doc spend
- **UM** `Claude` 2026-09-08 — IN PR #1428 — iOS chart-range label/data mismatch + fake Qdrant status line (board `303b352a`, branch `claude/um-range-and-vector-store`, worktree `~/apps/usage — range-fix`). Two independent reviewers flagged #1414 at merge commit `fdb4f5ef`. iOS: `PortfolioHistoryStore` flips `timeframe` synchronously on chip tap but kept the OLD range's summary during the reload
- **UM** `Claude` `Sentry` 2026-09-08 — IN PR #1460 — Crons in-progress check-in at scheduled-run start (board `c630ceed`, FLEET-INFRA-CB follow-up, branch ` -crons-inprogress-checkin`, worktree `~/apps/usage — crons-inprogress`). `scripts/sentry-ci-report.py` only sends a — Crons check-in after a scheduled `workflow_run` completes, so `checkin_margin` had to cover GitHub dis
- **AR** `Grok` `Sentry` 2026-09-08 — COMPLETED/MERGED #162 — macOS/web DSN split (board `f479c056`, branch ` -macos-web-dsn-split`, worktree `~/apps/autorotate — macos`). Mirror ContactLogo PR #67. Mac — Cocoa; Infisical `SENTRY_DSN_MACOS` injects into Mac `SENTRY_DSN`. iOS unchanged
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Issue #37 drop dead Simple Icons slugs + liveness CI (board 32be84ad, worktree `~/apps/contactlogo — simpleicons` @ `fix/simpleicons-liveness`). 23 CDN-404 slugs removed from web/Swift/Kotlin maps; chase.com remapped to live slug `chase`; weekly `simpleicons-liveness.yml` added. Rebased onto main 2026-09-08 keeping `jpmorganchase.com→chase` and dropp
- **BF** 2026-09-08 - BF-DESIGNER - IN_PROGRESS - Sidebar: reorder contexts, Bot Chats, recency, engine logos, merge threads; RAG timeout. <! — wb-agent-report:2d627f55356c4795ac0679e0c054bdbc — >
- **BF** `Antigravity` `Gemini` 2026-09-08 — BF-FIXER — IN PROGRESS — quotas — + Third-Party only; Bot Profile avatar drag-drop (board `2bf6c493`, branch `fixer/quota — avatar-drop`, worktree `~/apps/botfleet-fixer-quota-avatar`). Two shared numbers, not per-model rows. Avatar box accepts GIF, HEIC, BMP, SVG and existing formats. No TestFlight. <! — wb-agent-report:2bf6c493a56943768e4b32185599
- **BF** `Claude` `Codex` 2026-09-08 — PLANNED - HTTP tool executor: five P2 follow-ups from the — re-review of #236 (all confirmed on main). <! — wb-agent-report:049bad66db014723a0c1538149f8e077 — >
- **BF** `Claude` `Grok` 2026-09-08 — PLANNED - HTTP tool executor (#236): rejected dispatch is swallowed so the bot never leaves working, and the tool_calls: prefix collides with the — driver. <! — wb-agent-report:5d67971ed432466faa48571757901e21 — >
- **BF** `Claude` 2026-09-08 — PLANNED - HTTP tool executor: 60s listener timeout abandons slow MiniMax/OpenAI-compat rounds and hangs the bot. <! — wb-agent-report:29a2bdfefe1d4d98984dd4d3243469be — >
- **BF** `Claude` 2026-09-08 — PLANNED - HTTP tool executor: round cap leaves the bot busy until the 20-minute stall watchdog. <! — wb-agent-report:677de64466954b538ab1a815041c1618 — >
- **BF** `Claude` `MiniMax` 2026-09-08 — PLANNED — first-class engine: driver-owned tool loop on a shared chat-completions base (design A, 11 PRs). <! — wb-agent-report:4564fe5eebda442baa3caf43da144701 — >
- **BF** `Claude` `MiniMax` 2026-09-08 — IN_PROGRESS — PR9: — price table, real cost, observability span. Branch -09-prices-cost-span, worktree ~/apps/botfleet — 09. <! — wb-agent-report:264770eecc15459f8630347c9ac89508 — >
- **BF** `Claude` 2026-09-08 — IN PR #258 — config.json lost-update race between Electron and server (PR #251 review) (board `a2a3a586`, branch `claude/config-lock`, worktree `~/apps/botfleet — config-lock`). Shared advisory file lock around every config.json read-modify-write (server saveConfig, Electron recordAutomaticCheck, boot credential migrations) plus a two-process regression test
- **BF** 2026-09-08 — BF-COMPILER — DEPLOYED — iOS composer on TestFlight 1.0.39 / 202609081436 (board `e92b04b5`, PR #238 squash `114ca1a9`). Hosted ios-ship run 34239286614 uploaded from origin/main. VALID, IN_BETA_TESTING. Phone still on 1.0.38 needs a TestFlight update. Did not extra-ship. <! — wb-agent-report:e92b04b5afcb40d3a7f1b0a441775b92 — >
- **BF** `Grok` 2026-09-08 — IN_PROGRESS - Settings Models layout: larger dialog, wrap pills, iOS stacked fallbacks. <! — wb-agent-report:991b22a3d5414296afcbcd1b21ea55c8 — >
- **BF** `Claude` `Sentry` 2026-09-08 — DEPLOYED (#249, Mac harness 11:01Z, vault=13 applied=5) — BotFleet sources every secret possible from Infisical (BotFleet prod `836aebe2…`, automation machine identity): harness boot preload into env, desktop shell, CI workflows, Mac install migration (board `26e37b1f`, branch `claude/infisical-secrets` stacked on ` -usage-telemetry`, worktree `~/apps/bot
- **BF** `Grok` 2026-09-08 — IN PROGRESS — Designer UI copy only on remaining PRs after #240 Title Case (boards `6ce09e3d` `#237`, `57910d13` `#231`, `e92b04b5` `#238`). Title Case `Update From This Mac`, `Cloud Desktop` / `Cloud Provider` (keep This Mac / My VPS), composer rollout heading. Extra-ship no. No functional/server
- **BF** `Claude` `Sentry` 2026-09-08 — DEPLOYED (#247, Mac harness 11:01Z) — receives zero BotFleet telemetry: harness has no DSN, renderer bundle inert, iOS `secrets.SENTRY_DSN` missing; audit Usage Monitor stream (board `f7293d06`, branch ` -usage-telemetry`, worktree `~/apps/botfleet — `). DSN saved to a chmod 600 handoff file (never printed). Plan: config-driven `obse
- **BF** `Grok` 2026-09-08 — IN PROGRESS — Fixer: address unresolved review threads on PRs 240 238 237 236 231 (board `1e657d54`). Push fixes onto PR branches. Do not merge. #233 Monthly usage dedupe already resolved in `2db2fd68`. <! — wb-agent-report:1e657d542be94bcc85185e7961ca1e22 — >
- **BF** 2026-09-08 - BF-DESIGNER - IN_PROGRESS - iOS: ST app save fails on ghost room member; queued X is no route. <! — wb-agent-report:e8a8e5f15e00403cb1b7ea8ee6f04c1b — >
- **BF** `Grok` 2026-09-08 — BF-DESIGNER — IN PROGRESS — iOS ST app save unknown room member + queued X no route (board `e8a8e5f1`, branch `grok/ios-save-queue`, worktree `~/apps/botfleet — save-queue`). PATCH drops leftover deleted-bot roster ghosts so a phone save is not blocked. Packaged companion 1.0.30 still 404s DELETE /queue/; source already allowlists it (#224). No TestFlight. Ask be
- **BF** 2026-09-08 — BF-COMPILER — IN PR — Bot-to-bot chats out of Apps/Channels; restore ubf checkout; local Update when GitHub has no latest-mac.yml (board `6ce09e3d`, branch `compiler/bot-chats-sidebar`, worktree `~/apps/botfleet-compiler-ubf`). Detached `~/apps/botfleet-server` restored so `ubf` works. No TestFlight upload
- **BF** 2026-09-08 - BF-COMPILER - IN_PROGRESS - Bot-to-bot chats land in Apps/Channels; ubf checkout missing. <! — wb-agent-report:6ce09e3d84164aca9509e8cbb98b41e3 — >
- **BF** `Claude` 2026-09-08 — PLANNED - settings-rev2 C (#219): the 6-hour auto-update throttle never persists, plus two P2 defects. <! — wb-agent-report:2a77066b65ab4c69851808286f8e83ee — >
- **BF** `Claude` `MiniMax` 2026-09-08 — IN_PROGRESS — PR1: HTTP-lane fixtures, — stream hardening, honest engine metadata. <! — wb-agent-report:aad7d97067334b0bb370e4e8ea3581d1 — >
- **BF** `Claude` 2026-09-08 — PLANNED - settings-rev2 A (#220): three P1 + three P2 defects confirmed on main. <! — wb-agent-report:ff8dd5501b984e8491ef13b593f00bd3 — >
- **BF** `Claude` 2026-09-08 — PLANNED - Computer allowlist is bypassed for unconfigured bots: resolveGrants returns the UNFILTERED set when the intersection empties. <! — wb-agent-report:315b1fd7083844f1b175fff476218454 — >
- **BF** `Claude` `MiniMax` 2026-09-08 — IN_PROGRESS — PR2: driver-owned tool loop, — emits one terminal event per turn. <! — wb-agent-report:838bf3c55f3e41ad92472b8ecb3ebe46 — >
- **BF** `Claude` 2026-09-08 — PLANNED - settings-rev2 B (#218): DeepSeek balance credential is dead in the packaged app, and /api/quotas blocks on an unbounded fetch. <! — wb-agent-report:01f4994a33e0493382e095c74d7a88be — >
- **BF** `Claude` 2026-09-08 — IN_PROGRESS - [BF] BotFleet must source every secret possible from Infisical (BotFleet prod, automation machine identity): harness runtime, desktop shell, CI workflows, plus migration of the Mac install's stored keys. <! — wb-agent-report:26e37b1fb3794bffbe2e2b932cb273ca — >
- **BF** `Claude` `Sentry` 2026-09-08 — IN_PROGRESS - [BF] — gets zero telemetry: harness has no DSN, web bundle inert, iOS secret missing; audit Usage Monitor stream. <! — wb-agent-report:f7293d0631c04e4d9a9d04d68f3fee83 — >
- **BF** `Antigravity` `Gemini` 2026-09-08 — BF-FIXER — COMPLETED — quotas — + Third-Party only; Bot Profile avatar drag-drop. PR #246 squash `3a5f57c1`. Board `2bf6c493`. Two shared numbers, not per-model rows. Avatar box accepts GIF, HEIC, BMP, SVG and existing formats. Group min skips exhausted 0% models. No TestFlight. Mac app needs `update-botfleet.sh`. <! — wb-agent-report:2bf6c493a56943768
- **BF** 2026-09-08 — BF-FIXER — COMPLETED — BOTFLEET-2 EADDRINUSE 127.0.0.1:8793. PR #248 squash `f5dcf46d`. Board `dd86060b`. Named EADDRINUSE handling so a bind collision is not an uncaught fatal. 8791-8793 are named after collision, not reserved before bind. Live seat-mcp 8793 and BotFleet 8799 still 200. No TestFlight. <! — wb-agent-report:dd86060b15d346e5ade856183fa42d18 — >
- **BF** `Claude` 2026-09-08 — IN_PROGRESS - Mac download links on botfleet.app, README, and docs point at BotFleet-1.0.30 filenames no release carries; move to stable BotFleet.dmg names on the app repo. <! — wb-agent-report:2b054fbd7f5c45a9994288eee70da9f0 — >
- **BF** `Claude` 2026-09-08 — IN_PROGRESS - Restore the original DeepSeek mark viewBox (owner ruling Sep 8). <! — wb-agent-report:eaa9441ce73a48fea1e0c16053b1b8cb — >
- **BF** 2026-09-08 — BF-FIXER — COMPLETED — Simple-mode merge-all + iMessage trigger cards / [to iMessage] gated replies. PR #245 squash `25c010aa`. Board `8bfc6b0b`. Switching to Simple offers Merge All Threads or Keep Extra Threads Hidden. iMessage inbound renders as a Mac-style trigger card (`[from iMessage]`); only `[to iMessage]` bot replies are relayed, tag stripped. Relay LaunchAgent
- **BF** `Sentry` 2026-09-08 — BF-FIXER — COMPLETED — Webhook payloads as collapsible cards; fleet-infra — to Plumber. PR #239 squash `e938e7d6`. Board `28f76152`. — named hooks with project.slug fleet-infra go to Plumber. Web + iOS Details card, not a blue user bubble. No TestFlight. Mac harness needs `update-botfleet.sh`. <! — wb-agent-report:28f761520dc14cfa92221aa68f2a3cbd — >

## 2026-09-07

*0 PRs merged · 0 issues opened · 0 issues closed · 5 effort rows*

### Effort board

- **CT** `Antigravity` 2026-09-07 — COMPLETED/DEPLOYED #2333 (`dc5f1827`) — Account dropdown section hierarchy and spacing (board `c415c430`, branch `antigravity/account-menu-section-hierarchy`). Enlarged account menu section headings (`.menu-section-label`) from 11px to 15px uppercase bold and added 16px top margin between sections. Tuned menu buttons and links to 13.5px with comfortable 9px padding and 9px
- **CT** `Antigravity` 2026-09-07 — COMPLETED/DEPLOYED #2334 (`5164a3d4`) — Fix House not_found ingestion phantoms, Senate paper viewing, and example form row extraction (branch `antigravity/fix-phantom-ingestion-and-senate-docs`). Unblocked House official filings (Cisneros `20035190`, Taylor `20035146`/`20035392`, and 876 historical probe collisions) via upgrade path in `insertFilingIfNew`, reconciler recover
- **DD** `Antigravity` 2026-09-07 — COMPLETED — Fix Vercel auto-deploy rate-limit query (&state=READY) (branch `ag/vercel-ignore-state-ready`, worktree `~/apps/dealdex — vercel-fix`)
- **PS** `Antigravity` 2026-09-07 — COMPLETED/DEPLOYED — Update BotFleet app logo (bf.png), remove Socratic Trade TestFlight links, and polish app descriptions (PR #65 merged `364dad1`). Deployed to production (`dpl_FV5tML6Y5oq1mDyf8hNHFBtZX3Ve`) on `https://jays.services`. Verified live HTTP 200, `bf.png` 200, ST TestFlight removed, app blurbs refreshed
- **PS** `Antigravity` 2026-09-07 — COMPLETED/DEPLOYED — Fix Vercel auto-deploy rate-limit query (&state=READY) (PR #63 merged `ffa9d90`). Added &state=READY filter to `site/vercel-ignore-hourly.sh` and updated Vercel dashboard ignoreCommand fallback to `exit 1`. Verified live production deployment on `https://jays.services` (HTTP 200)

## 2026-09-06

*0 PRs merged · 0 issues opened · 0 issues closed · 1 effort rows*

### Effort board

- **CT** `Grok` 2026-09-06 — IN PR — Harden fleet-sqlite-backup.sh: in-script flock, complete-only retention, sqlite3 .backup timeout (board `e1f66898`, branch `grok/sqlite-backup-harden`, worktree `~/apps/congress — backup`). Housekeeper already mitigated live (killed overlapping ST `sqlite3 .backup`, deleted incomplete locals, cron `flock -n /var/lock/fleet-sqlite-backup.lock`). Product s

## 2026-09-04

*0 PRs merged · 0 issues opened · 0 issues closed · 20 effort rows*

### Effort board

- **CT** `Grok` `Sentry` 2026-09-04 — COMPLETED/DEPLOYED #2316 (`80174cb2`) — max-features: restore nosniff + HSTS after — resolver throw (board `af1ab6e9`, branch ` -max-features`, worktree `~/apps/congress — max`). CI 33880922698: `resolveSentryBrowser(undefined)` threw on `env.SENTRY_DSN` and skipped header attach. Replay stays error 100% / session 10%. No merge/ship. Roll
- **CT** `Grok` 2026-09-04 — COMPLETED/DEPLOYED #2315 (`84521968`) — Admin Premium roster: trial vs paid, Stripe vs Apple (board `43eaac7f`, branch `grok/admin-premium-roster`). Diagnostics lumped trial+paid as Subscribed and skipped Apple. Stale `trialing` after the Sep 3 $5 charge (batch EXISTS miss + basil invoice id). Roster shows email, plan, Trial or Paid, Stripe or Apple, Sandbox or Productio
- **CT** `Grok` 2026-09-04 — COMPLETED/DEPLOYED #2313 (`b1eff6b0`) — FMP lease reclaim after Mac scout retirement (board `d09acd0a`, branch `grok/fmp-reclaim-dead-scout`, worktree `~/apps/congress — exec-health`). #2307 live (`d4e5cc4a`) still logged `fmp (handed_off)` every tick. needScout stuck true after proxy 429s; Mac scout gone; server never reclaimed a null lease. Server now probes whe
- **CT** `Grok` 2026-09-04 — DEPLOYED #2307 (`d4e5cc4a`) — FMP latency ERROR 42h silent + duplicate Exec Source Health rows (board `d09acd0a`, branch `grok/fmp-exec-health`). Dual free-tier keys direct; 429 retries other key then one Senate-proxy hop. RapidAPI has no house/senate (404) and no OGE/executive (400/404). UW/QQ retired until paid/trial. Source Health maps oge+executive to one Exec row
- **CT** `Grok` 2026-09-04 — COMPLETED/DEPLOYED #2306 (`8193f7c1`) — Swap Rising Activity / Top Performers, full-bleed filter bar, Trades column defaults (board `1f0f2bd4`, branch `grok/trends-layout-cols`, worktree `~/apps/congress — layout`). Owner: first Trends pair cramped; later pair had room. Rising Activity moves next to Most Active; Top Performers next to What Is Being Traded. Filt
- **CT** `Grok` 2026-08-05 — COMPLETED + DEPLOYED — Pricing $5/$50 + 30d trial, delivery edit, Apple IAP. PR #1345 `0733b3f8`. Live HTML: $5/mo · $50/yr · 1-month free trial. Coolify deploy finished. grant-premium jaywedgeworth22@gmail.com → trialing monthly thru 2026-09-04 + seeded user SSE delivery. ST system deliveries (socratic-trade-) left alone. iOS IAP still needs App Store Connect produ
- **UM** 2026-09-13 — FX — IN PROGRESS — Local Import Package tap swallowed by Merge/Replace picker (board `b4ebf716`, branch `fx/local-import-tap`, worktree `~/apps/usage-fx-import-tap`). Owner cannot tap Import Package in Usage Local Monitor; a List Picker for Merge / Replace All still steals the button (the 2026-09-04 split-into-separate-views fix was not enough). Website Download For Local JSON i
- **UM** `Grok` `Sentry` 2026-09-04 — IN PR #1418 — Usage enrichment via stats_v2 (board `c081199a`, SHA `aefe2e95`, branch ` -usage-enrichment`, worktree `~/apps/usage — usage`). Official org stats only: Errors / Transactions / Replays / Attachments / Profiles / Monitors, accepted and rate-limited. No public API for prepaid credit, remaining sponsored balance, reserved quota, PAYG
- **UM** `Grok` 2026-09-04 — IN PR #1417 — Product litestream.yml L1-only so next bake keeps L2/L3 off (board `d784035ed4c24a43a74565323cc8e152`, issue #1416, SHA `44f8b1a8`, branch `grok/litestream-l1-only`, worktree `~/apps/usage — l1`). Housekeeper overlay already holds live L2/L3 off; repo `litestream.yml` still omitted `levels:` so DefaultConfig would restore them on bake. Single `
- **UM** `Grok` `Sentry` 2026-09-04 — IN PROGRESS — max-features: Feedback widget + server profiling (board `af1ab6e9`, branch ` -max-features`, worktree `~/apps/usage — max`). Replay stays 10%/100%. Kill switch `NEXT_PUBLIC_SENTRY_FEEDBACK_ENABLED=false`. Rollout: `docs/rollouts/2026-09-04 — max-features.md`
- **UM** `Grok` `Antigravity` `Gemini` 2026-09-04 — IN PROGRESS — usage N/A remaining is 0 not unknown (board `a2bb5579`, branch `grok/quota-na-exhausted`, worktree `~/apps/usage — routing`). Owner: none remains. Skip
- **DD** `Grok` `Sentry` 2026-09-04 — COMPLETED — max-features: iOS profiling + Session Replay + Android native (board `af1ab6e9`, branch ` -max-features`, worktree `~/apps/dealdex — max`). Android ENABLE (masked Replay 10%/100% error, profiling 0.1). Rollout: `docs/rollouts/2026-09-04 — max-features.md`
- **DD** `Grok` `Sentry` 2026-09-04 — COMPLETED — Performance child spans on Nitro/API scan hops (board `9fb9cccafb9c40b889466516a18e8dd5`, branch ` -scan-hop-spans`, worktree `~/apps/dealdex — hop-spans`). Spans: `scan.ebay`, `scan.mercari`, `scan.match`, `scan.enrich`, `scan.cache.hit`, `scan.cache.miss`. Datadog stays `web.request` only. Extra-ship no. Local gates green (
- **DD** `Grok` 2026-09-04 — COMPLETED — ios-ship NativeAuth.swift Swift 6 main-actor isolation after #271 (branch `grok/ios-nativeauth-mainactor`, worktree `~/apps/dealdex — nativeauth`). Archive rc=65 on run 33721859665. Hop `AppleSignInDelegate` init/held onto MainActor. Board `bce3ad82869f4f438851f60bdcf85145`. No extra-ship. No ` — force-ship`
- **AR** `Grok` `Sentry` 2026-09-04 — COMPLETED/MERGED #148 — max-features: Web Feedback, iOS Error Replay, Android Native
- **CL** `Grok` 2026-09-04 — BF-DESIGNER — IN PROGRESS — ContactLogo.com landing headings and buttons Title Case (board `62acf520`, issue #63, branch `grok/web-title-case`, worktree `~/apps/contactlogo — case`). Web chrome only. No TestFlight. Rollout: `docs/rollouts/2026-09-04-web-title-case.md`
- **AFC** `MiniMax` `Grok` `Cursor` 2026-09-04 — IN PROGRESS — Slack tag is ; DeepSeek Harness is DSH (` -dsh-acronyms`, worktree `~/apps/fleet — dsh`, board `f9df420d`). Owner 2026-09-04: anywhere a — acronym is used, it is ` ` (Slack ` `; former ` ` retired). DeepSeek Harness is `DSH` (Slack `[DSH]`; former harness tag `DEEPSEEK` retired). — running a DeepSeek model stays
- **AFC** `Grok` `Sentry` 2026-09-04 — IN PROGRESS — max-features fleet (branch ` -max-features-fleet`, worktree `~/apps/fleet — max-features`, board `af1ab6e9`). Designer rulings UPDATE: PS/CTS/OPS omit — (approved); ST+CT web Replay error 100%/session 10%; Seer Autofix ENABLE BotFleet only; Android ENABLE for DD/AR/CL. AFC is docs/matrix only (not a product — target). No
- **AFC** `Claude` 2026-09-04 — COMPLETED/MERGED #189 — Fleet UI standard: nothing truncated without recourse (`claude/no-silent-truncation-standard`, worktree `~/apps/fleet — truncation`, board `ecab7748`). Owner ruling 2026-09-04: any text the UI clips must show its full value on hover, on every app. Errors are the strict case. Truncate in CSS, never `.slice(0, N)` — a string shortened in code
- **AFC** `Claude` `MiniMax` 2026-09-04 — COMPLETED/MERGED #187 — Coordinator acronym is `AFC` everywhere; onboarding phase numbering; — recall slot (`claude/docs-onboarding-phases`, worktree `~/apps/fleet — `, board `43c7493f`). Owner ruling 2026-09-04: the coordinator is `AFC`, never `AFL` and never `FLEET` — `[SEAT->FLEET]` is a broadcast wake that costs every seat time, so it must not doubl

## 2026-09-03

*0 PRs merged · 0 issues opened · 0 issues closed · 13 effort rows*

### Effort board

- **CT** `Grok` 2026-09-03 — COMPLETED/DEPLOYED #2304 (`297226b1`) — iOS Manage Subscription for website/Stripe Premium (board `589b9fe3`, branch `grok/ios-stripe-manage-sub`). Account sheet 401 told web subscribers to sign out. Root cause: `POST /billing/portal` was cookie-only; iOS already sends Bearer. Server accepts Bearer; Stripe/`nil` portal failure opens `/?billing=manage` instead of sign-out
- **CT** `Grok` 2026-09-03 — COMPLETED/DEPLOYED #2305 (`b4973ce3`) — Retarget AppUpdatePrompt off ios-app-versions (board `ca104839`, branch `grok/ios-versions-home`, worktree `~/apps/congress — versions`). Public manifest is `ai-fleet-coordinator` `site/ios-versions.json`. Personal-Site does not list the old repo. Rollout: `docs/rollouts/2026-09-03-ios-versions-home.md`
- **CT** `Grok` 2026-09-03 — COMPLETED/DEPLOYED #2303 (`bdb373b3`) — Stop CT twice-hourly TestFlight spam (board `f9d5c319`, issue #2302, branch `grok/ios-ship-schedule-gate`, worktree `~/apps/congress — ship-gate`). Hosted macos-latest has no last-ship file; cron treated that as a first ship and uploaded 1.0.222. Workflow disabled_manually. Scheduled ticks with no last-ship now skip. Claime
- **CT** `Grok` 2026-09-03 — / BF-Publisher — COMPLETED/DEPLOYED #2301 (`04116d27`) — Drain 4 Senate paper PTRs parked on IBM/MSFT form samples (board `2d6f4302`, branch `grok/publisher-senate-paper-samples`, worktree `~/apps/congress — senate-samples`). Live: confirmed Blumenthal `S-a3722489` 38 spouse lots and `S-16afdd38` 21 spouse lots; confirmed Boozman `S-7dfcd5fd` 8 IRA lots and `S-5
- **UM** `Grok` 2026-09-03 — IN PROGRESS — Retarget AppUpdatePrompt off ios-app-versions (board `ca104839`, branch `grok/ios-versions-home`, worktree `~/apps/usage — versions`). Public manifest is `ai-fleet-coordinator` `site/ios-versions.json`. Client + Local copies stay byte-identical to the pin. Rollout: `docs/rollouts/2026-09-03-ios-versions-home.md`
- **UM** `Grok` `Gemini` `Antigravity` 2026-09-03 — IN PROGRESS — Quota windows + ` -usage quota — json` collector (board `109294fe`, issue #1411, branch `grok/quota-routing`, worktree `~/apps/usage — routing`). Per-model remaining, honest — N/A, `GET /api/quota-windows` skipModelTypes for BotFleet
- **UM** `Grok` `Codex` `Cursor` 2026-09-03 — IN PR #1409 — Agents seats from receipts + observed — Plus, window chips (branch `grok/seat-plans`, worktree `~/apps/usage — plans`, board `b866649c`, issue #1407). Window chips are 5h/24h/7d/30d/All Time with gap-4. — plan is observed from local login JWT (plus), not guessed Pro $200. Copilot not billed. — Ultra included with SuperGrok Heavy. Mini
- **UM** `Grok` `Antigravity` 2026-09-03 — IN PROGRESS — $70 net seat + honest missing telemetry (branch ` -seat-telemetry-honesty`, worktree `~/apps/usage — telemetry`, board `7fd199f9`, claimed: Wed, Sep 3, 2026). Owner: $100 Google AI Ultra plan of which $30 was already Google One, so $70 net for the AI. Agents tab must say not reported instead of pretending little/no usage when
- **DD** `Grok` 2026-09-03 — MERGED #273 — Retarget AppUpdatePrompt off ios-app-versions (board `ca104839`, branch `grok/ios-versions-home`, worktree `~/apps/dealdex — versions`). Public manifest is `ai-fleet-coordinator` `site/ios-versions.json`. Pin and iOS target stay byte-identical. Rollout: `docs/rollouts/2026-09-03-ios-versions-home.md`
- **DD** `Grok` `Antigravity` 2026-09-03 — MERGED #271 — Pickup — cap: native Apple Sign In via ASAuthorizationAppleIDProvider (branch `ag/fix-apple-native-form-post`, worktree `~/apps/dealdex — apple-fix`). — hit usage cap mid-PR. Adopted uncommitted firstName/lastName payload, registered the route in `routeTree.gen.ts`. Squash-merged. ios-ship then failed on NativeAuth isolation (row above). Board `5
- **CL** `Grok` 2026-09-03 — BF-DIRECTOR / — IN PROGRESS — iOS TestFlight background crash: Swift 6 MainActor trap in BGTask handler (issue #59, board 35559745, worktree `~/apps/contactlogo — crash` @ `grok/bgtask-mainactor-crash`). `MatchBackgroundTask.register()` is nonisolated so iOS can launch overnight matching without `_dispatch_assert_queue_fail`
- **AFC** `Grok` 2026-09-03 — IN PROGRESS — Move iOS version manifest off ios-app-versions into this repo (`grok/ios-versions-home`, worktree `~/apps/fleet — versions`, board `ca104839`). Owner deleting the one-file public repo. Personal-Site does not list or fetch it. Canonical file `site/ios-versions.json`. Sibling PRs retarget AppUpdatePrompt + publish-ios-versions.sh. Rollout: `docs/roll
- **AFC** `Grok` 2026-09-03 — BF-DIRECTOR — IN PROGRESS — Owner copy: Title Case chrome + never display &nbsp; in cloud text (`grok/copy-cloud-nbsp`, worktree `~/apps/fleet — cloud`, board `09e01a3c`). FLEET-UI-COPY + sentence-gap + owner-copy. Product chrome routed to Designer/Builder. No TestFlight

## 2026-09-02

*0 PRs merged · 0 issues opened · 0 issues closed · 12 effort rows*

### Effort board

- **CT** `Claude` `Grok` 2026-09-05 — CLOSED remaining audit ranked items (boards `a8ac1f29`/`#2180`, `1d412c9b`/DLQ, `01e4e870`, `3a1622e2`). Owner asked to fully resolve the "still open" items from the — audit pickup below. Findings: (1) feed `order=desc` sort contract — already fixed by — itself 2026-09-01 in PR #2281 (`NEWEST_SNAPSHOT_ORDER_SQL`, dedicated regression test `newestSnapshotOrder
- **CT** `Antigravity` 2026-09-02 — COMPLETED/DEPLOYED #2295, #2296, #2297, #2298 (`0fb52bf4`) — Retire scout.jays.services relay, switch Senate/House scraping to Infisical residential proxy, fix Senate paper OCR parsing & batch-chunking, and reprocess all 81 failed Senate paper filings (1,000+ trades extracted & persisted)
- **CT** `Antigravity` 2026-09-02 — COMPLETED/DEPLOYED #2293 (`f8eb6d49`) — Fix Senate paper media scan loading, resolve Ingestion Dead Letter outbox failures, and explain Review Queue vs DLQ distinction (branch `antigravity/senate-paper-media-fix`)
- **UM** `Antigravity` 2026-09-02 — IN PROGRESS — Overview timeframe selection on Web and iOS (branch `feat/overview-timeframe-selection`). Adds timeframe selection control to the top of the Overview dashboard across Web and iOS apps, supporting 12/6/3/1 month rolling periods, current calendar month, and named prior calendar months
- **UM** `Claude` `Sentry` 2026-09-08 — IN PR #1430 — Crons `ci-usage-monitor-ios-testflight-ship-mac-runner` false-positive fix (board `c630ceed`, FLEET-INFRA-CB, branch ` -crons-margin-ios-ship`). GitHub's own schedule dispatcher for "iOS TestFlight ship (Mac runner)" (`13,43 `) lands 1.2-29.5min after its nominal minute (median 9.5min; 15/40 recent runs over 15min) even thou
- **DD** `Antigravity` 2026-09-02 — COMPLETED/MERGED #254 — Fix social auth: login page auto-dismiss + Apple Sign In JWT generation. Login card now navigates to callbackURL when session activates (closes the "popup" feel after Google/X sign-in). Apple Sign In auto-generates the ES256 client_secret JWT from raw key env vars (APPLE_TEAM_ID + APPLE_KEY_ID + APPLE_PRIVATE_KEY). Typecheck/lint/197 tests gre
- **PS** `Antigravity` 2026-09-02 — IN PROGRESS — Fix vercel-ignore-hourly watch_args pathspec for site subfolder (branch `ag/vercel-pathspec-fix`, worktree `~/apps/personal- `). Update watch_args to use :(top)site so git diff correctly detects site changes
- **CL** `Antigravity` 2026-09-02 — IN PROGRESS — Fix vercel-ignore-hourly watch_args pathspec for web subfolder (branch `ag/vercel-pathspec-fix`, worktree `~/apps/contactlogo — vercel-fix`). Update watch_args to use :(top)web so git diff correctly detects web updates
- **AFC** `Grok` 2026-09-02 — IN PROGRESS — Idle MCP unload 36h → 12h (`grok/idle-unload-12h`, worktree `~/apps/fleet — 12h`, board `09102247`). `/resume` reloads tools. `GROK_IDLE_UNLOAD_HOURS` for shorter trials
- **AFC** `Claude` 2026-09-02 — DEPLOYED — Fleet RAG as a memory platform every agent commits lessons to. Board `5c27dffd` (+ `0f9a13b1` doc diet via #175). Worktree `~/apps/fleet — rag` @ `claude/fleet-rag-platform`. Search: in-process grouping (one hit per doc, adaptive window), lesson-boost prefetch, cross-encoder rerank via new Coolify `tei-reranker` (MiniLM, 0.5 s / 30 candidates; bge-reran
- **AFC** `Grok` 2026-09-02 — IN PROGRESS — Fleet RAG adoption: every platform searches and contributes. Board `03ee6d8b`. Claimed Tue, Sep 2, 2026. Worktree `~/apps/fleet — mine` @ `grok/rag-adopt`. session-start 2b + closeout contribute; skills installed to all Mac seats. Product AGENTS.md next wave. Do not bulk-ingest chat dumps. Ingest lock still held by pid 81666 (apple-note)
- **AFC** `Grok` 2026-09-02 — IN PROGRESS — RAG write path: contribute lessons; chat scan is policy-only. Owner rejected DeepSeek read-only corpus. Branch `grok/rag-memory-policy`. `ingest — all` skips `chat-log`. Do not bulk-ingest staged session JSONL. Board `b24d3450` (ingest follow-on) retargeted

## 2026-09-01

*0 PRs merged · 0 issues opened · 0 issues closed · 53 effort rows*

### Effort board

- **CT** `Grok` 2026-09-01 — IN PROGRESS — Datadog Free-tier: webhook miss off warn, `prod`→`production`, LLMObs on OpenRouter (board `ad678866`, branch `grok/datadog-free-tier`, worktree `~/apps/congress — free`). Rollout: `docs/rollouts/2026-09-01-datadog-free-tier.md`
- **CT** `Grok` `Sentry` 2026-09-01 — IN PR — CT iOS Cocoa — (board `514c6531`, branch ` -ios-cocoa`, worktree `~/apps/congress — ios`). Adopted XcodeGen (`clients/ios/project.yml` + `xcodegen-post.py`). Added `SentryTelemetry.swift` (plist-only `SENTRY_DSN`, errors+crashes+hangs, no Replay/screenshots/PII). Follow-up: ios-ship dSYM lane (no new LaunchAgent). Rollout: `docs/rollouts
- **CT** `Grok` `Sentry` `Antigravity` 2026-09-01 — IN PR — fleet adoption leftovers: DSN out of git, PDF XRef ignoreErrors, sparse — Logs (board `58cae930`, branch ` -fleet-adoption`, worktree `~/apps/congress — adopt`). — #2282 already dropped `@sentry/cloudflare` and set traces 0.2. This lane empties committed `SENTRY_DSN`, rotated a new — key `production-2026-09` into Infisical + C
- **CT** `Antigravity` `Sentry` 2026-09-01 — IN PROGRESS — cleanup: drop dead Cloudflare SDK, align default trace sampling to 0.2, and clean typechecks (branch ` -cleanup-and-trace-defaults`). Removed legacy `@sentry/cloudflare` from `package.json` and `deno.json`, aligned fallback `tracesSampleRate` in `sentryRuntime.ts` to 0.2, and fixed PDF destroy cast in `autonomySweeps.ts`. Gate: `deno check` passe
- **CT** `Grok` 2026-09-01 — IN PROGRESS — August ops leftovers: P0 #2180 newest-first order, P1 #2182 dead-letter health split, NTR detector, stream 400 hint (board `a8ac1f29` `1d412c9b` `7bbb7cd8`, branch `grok/ops-review-open-items`, worktree `~/apps/congress — review`). Live verify: Apple webhook POST is mounted (`signedPayload required`, not 404). `order=desc` without `sort=` now uses `CO
- **CT** `Claude` 2026-09-01 — IN PR - Codify "Never idle-watch a PR" as a binding fleet rule (branch `claude/never-idle-watch-rule`). Owner ruling 2026-09-01: agents "should never just wait and watch for things to merge since that wastes tokens/time and they inevitably almost invariably end up slowly wasting money/quota while the PR sits there with conflicts or comments/issues unresolved." New `## N
- **CT** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — production deploy records (` -cli releases deploys new -e production`) (branch ` -deploys`, worktree `~/apps/congress — deploys`, board `2d1c8565`). Additive workflow on CI success for `main` push. VERSION = full git SHA matching Coolify `CT_BUILD_SHA` / `SOURCE_COMMIT`. No `releases new`. Soft-fail
- **UM** `Grok` 2026-09-01 — IN PROGRESS — Datadog Free-tier estimated-usage card + platforms probe (board `ad678866`, branch `grok/datadog-free-tier`, worktree `~/apps/usage — free`). Rollout: `docs/rollouts/2026-09-01-datadog-free-tier.md`
- **UM** `Grok` `Sentry` 2026-09-01 — IN PR #1394 (auto-merge armed) — Add — ci-report.yml so CI failures report to — `fleet-infra` (branch ` -ci-report`, worktree `~/apps/usage — ci`, board `83b8f820`, claimed: Mon, Sep 1, 2026). Copies CT-style additive reporter: fingerprint `[ci-failure, usage-monitor, workflow]`, branch is a tag only. Observes all UM workflows except Uptime M
- **UM** `Grok` `Sentry` 2026-09-01 — IN PR #1390 (auto-merge armed) — fleet adoption leftovers: client DSN bake, cron cadence, sparse logs/metrics (branch ` -fleet-adoption`, worktree `~/apps/usage — adopt`, board `fc5d6355`, claimed: Mon, Sep 1, 2026). `enableLogs` already true (#1389). Server tracing works. Zero client replays: `NEXT_PUBLIC_SENTRY_DSN` must be Coolify build-time
- **UM** `Antigravity` `Sentry` 2026-09-01 — COMPLETED (merged to `main`, #1389) — Structured Logs, normalized replay gates, and metrics split documentation (branch ` -logs-and-comment-fix`). Enabled `enableLogs: true` across server, edge, and browser — runtimes in Usage-Monitor, normalized `NEXT_PUBLIC_SENTRY_REPLAY_ENABLED` falsy checks, and updated — application metrics/health documentation
- **DD** `Grok` 2026-09-01 — COMPLETED/MERGED #229 (`76463b9`) — Living identity is DealDex.net / net.dealdex. README, PLAN, CONTRIBUTING, STATUS, native notes, tests, and audit identity block. Android package stays `me.grok.dealdex`. Fleet deploy-verify health landed in coordinator #161 (`6fbec1f`). Board `053cdba5` (audit continues)
- **DD** `Antigravity` `Sentry` 2026-09-01 — COMPLETED — iOS Native — Cocoa telemetry, crash reporting, and app-hang detection (branch `ag/ios — cocoa-expansion`). Integrates native — Cocoa SDK into DealDex iOS to capture uncaught crashes, OOMs, and 2.0s app-hangs: added — Cocoa SPM package dependency, implemented `SentryTelemetry.swift` for crash reporting and 0.2 distributed tracing, and wir
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED - Android: official io.sentry: -android crash+ANR (DSN from BuildConfig/env). <! — wb-agent-report:c56621e1cf6e4bac96475383e5f2d219 — >
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #243 — Android official — SDK (crash+ANR, no default PII) (board c56621e1). Card/desk data stays out of events. `./gradlew test` + verify SUCCESS
- **DD** `Grok` 2026-09-01 — COMPLETED - [DealDex] Vendor ios-fleet ship-testflight dSYM/Sentry inject. <! — wb-agent-report:88650b3fe4c9461e8f2e5ca010dcc5ca — >
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #240 — production deploy records (` -cli releases deploys new -e production`). Vercel integration lacked deploy markers; workflow added. Board `2d1c8565`
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #238 — Add fleet — ci-report.yml + scripts/sentry-ci-report.py (branch ` -ci-report`, worktree `~/apps/dealdex — ci`, board `b667e612`). Gold copy UM PR #1394. APP=`dealdex`. Fingerprint `[ci-failure, dealdex, workflow]`. <! — wb-agent-report:b667e612 — >
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED — DSN hygiene: no hardcoded iOS fallback. Merged iOS — DSN hygiene PRs (plist-only / no hardcoded ingest URL fallback). <! — wb-agent-report:7e18a8e4bb75488ca891a94d84033679 — >
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED — DealDex/BotFleet: prod DSN, Replay, Feedback, agent tracing. <! — wb-agent-report:d3f01c60eb4f457c855af60b4c196706 — >
- **DD** `Grok` 2026-09-01 — PLANNED - iOS pbxproj missing SentryTelemetry.swift Sources membership (ios-ship red). <! — wb-agent-report:9dd5fa7786a6428b9162000bc11c55a7 — >
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #223 (`e46f0fd`) — Add SentryTelemetry.swift to committed iOS Sources so TestFlight archive compiles. PBXBuildFile `6E68536A0591E1EAA8F9DF30`, PBXFileReference `BF5CF2870999472BC27D2F40`, group child, Sources phase, — cocoa SPM. Landed on `main` (the branch scheduled ios-ship checks out). No extra-ship. No ` — force-ship`. Board `9dd5fa7786a
- **DD** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #223 (`e46f0fd`) — Add SentryTelemetry.swift to committed iOS Sources so TestFlight archive compiles. PBXBuildFile `6E68536A0591E1EAA8F9DF30`, PBXFileReference `BF5CF2870999472BC27D2F40`, group child, Sources phase, — cocoa SPM. Landed on `main` (the branch scheduled ios-ship checks out). No extra-ship. No ` — force-ship`. Board `9dd5fa7786a
- **PS** `Grok` 2026-09-01 — IN PROGRESS — Datadog Free-tier fail-closed: `prod`→`production`, error-only logs, us5 fallback (board `ad678866`, branch `grok/datadog-free-tier`, worktree `~/apps/personal — free`). Rollout: `docs/rollouts/2026-09-01-datadog-free-tier.md`
- **PS** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #49 — Personal-Site stays Datadog-only; no — project (` -datadog-only`). Board `ca3e27f0`. Worktree `~/apps/personal — docs`. Explicit README/AGENTS sentence. Tiny unhandled-window-error — project is not wanted. Preserve `Earlier work included` and the Doximity `/profiles/…/view` URL. Slack `#agent-sync` post skipp
- **PS** `Grok` 2026-09-01 — IN_PROGRESS - Vercel auto-deploys skip unless site files changed, plus 1/hour (branch `grok/vercel-site-watch`, worktree `~/apps/personal — watch`). Board `46837afd`. Script watches `site/`
- **PS** `Grok` 2026-09-01 — COMPLETED — Cap automatic Vercel deploys to one production build per hour. Board `9051c3ac`. PR #53. Follow-up is site-file watch on `grok/vercel-site-watch`
- **AR** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #143 — Android official — SDK (crash+ANR, no PII/request bodies) (board 1fe88b1d, worktree `~/apps/autorotate — android` @ ` -android`). Owner un-deferred Android. Secrets app: `RequestSize.NONE`, no screenshots/view hierarchy
- **AR** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #141 — Add fleet — ci-report.yml + scripts/sentry-ci-report.py (branch ` -ci-report`, worktree `~/apps/autorotate — ci`, board `a37932ef`). Gold copy UM PR #1394. APP=`autorotate`. Fingerprint `[ci-failure, autorotate, workflow]`. <! — wb-agent-report:a37932ef — >
- **AR** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #134 — Web — SDK + rotation cron/metrics (board 12ccfa7e, PR #134, worktree `~/apps/autorotate — adopt` @ ` -fleet-adoption`). `@sentry/react` client (DSN-gated, sendDefaultPii false, replay 100% error / 0% session, no feedback widget) plus `@sentry/node` for scheduler cron + `rotation.success`/`rotation.fail`. Android Sent
- **CL** `Grok` 2026-09-01 — IN_PROGRESS - Vercel auto-deploys skip unless site files changed, plus 1/hour (branch `grok/vercel-site-watch`, worktree `~/apps/contactlogo — watch`). Board `46837afd`. Script watches `web/`
- **CL** `Grok` 2026-09-01 — COMPLETED — Cap automatic Vercel deploys to one production build per hour. Board `9051c3ac`. PR #56. Follow-up is site-file watch on `grok/vercel-site-watch`
- **CL** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — Android official — SDK (crash+ANR, privacy-safe, BuildConfig DSN) (board a571e9f7, worktree `~/apps/contactlogo — android` @ ` -android`). Owner un-deferred Android. `io.sentry: -android` 8.54.0; empty `SENTRY_DSN` no-ops; no screenshots/view hierarchy
- **CL** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — Add fleet — ci-report.yml + scripts/sentry-ci-report.py (branch ` -ci-report`, worktree `~/apps/contactlogo — ci`, board `c0a9829e`). Gold copy UM PR #1394. APP=`contactlogo`. Fingerprint `[ci-failure, contactlogo, workflow]`. <! — wb-agent-report:c0a9829e — >
- **CL** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — Web — SDK (`@sentry/browser`, DealDex Vite helper pattern) + `logo.match` metric (board 86902ab6, PR #52, worktree `~/apps/contactlogo — adopt` @ ` -fleet-adoption`). Replay 100% error / 10% session, feedback widget on, sendDefaultPii false. Android — is iOS-only until Android ships
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Native shells: surface retryable match rows instead of Not found (board 0eceafd5, issue #33, worktree `~/apps/contactlogo — retryable` @ `grok/native-retryable-rows`). Badge + Retry on the Not-found row. Web copy `No logo found` for true misses. No fourth bucket. PR #50
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Persist the iOS background review queue before notifying (board f91039fc, issue #32, PR #45, worktree `~/apps/contactlogo — issue32` @ `grok/persist-review-queue`). Codable `MatchResult`, `ReviewQueueStore` JSON in Application Support, write in `BackgroundMatchRunner.run()` before `setTaskCompleted` and before the notification, restore on `ReviewSess
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Android P1: undo last batch, stop candidate wrap, Select High, brand mipmaps (board 79e358ef, issue #43, worktree `~/apps/contactlogo — p1` @ `grok/android-p1-gaps`). Port kit UndoLog to app-private storage, Ready chip filters only, no `%` candidate wrap, Swap launcher mipmaps, versionName 1.0.1
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Web review UX: lock card height + human triage chrome (board efe8cdfb, issue #35, worktree `~/apps/contactlogo — ux` @ `grok/web-review-ux`). Virtualizer assumes uniform rows; CSS locks `.card` height and truncates. Approve is primary; Crop/Upload/Paste sit behind Choose your own. J/K/A/S/U triage. Settings HD-key empty-state
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Domain-keyed first-party logo cache on Vercel (board 72a48e35, issue #44, worktree `~/apps/contactlogo — cache` @ `grok/first-party-logo-cache`). `GET /api/logo/:registrableDomain`. No address books. Web engine tries the cache first; native stays on live CDNs this PR
- **CL** `Grok` 2026-09-01 — IN PROGRESS — Full-stack audit + remediations (board 1d89d23b, issue #41, worktree `~/apps/contactlogo — audit` @ `grok/full-stack-audit`). Trust surfaces, Simple Icons liveness, PWA/SEO, and native follow-ups from the 2026-09-01 owner audit
- **AFC** `Grok` 2026-09-01 — IN PROGRESS — Unload — MCP on chats idle >36h; grow Hetzner swap for RAM oversubscribe (`grok/idle-chat-unload`, worktree `~/apps/fleet — unload`, board `8247aa02`). `session/close` keeps transcripts. Hourly launchd `com.jay.grok-idle-unload`. Host `ensure-swap.sh` target 16GiB + swappiness 20
- **AFC** `Grok` `Claude` 2026-09-01 — IN PROGRESS — Pickup — cap: fleet RAG operational (`claude/fleet-rag-operational`, worktree `~/apps/fleet — rag`). Boards `c799b564` (recall interface) / `9c75471c` (slice 1 ingest) / `0f9a13b1` (slice 2 guardrails). Code landed on the branch; `recall doctor` green (read-only key mode, 8 seed points at start); first full ingest running. Slack skipped (`account_
- **AFC** `Grok` 2026-09-01 — IN PROGRESS — DSH Dock WKWebView (branch `grok/dsh-dock-webview`, worktree `~/apps/fleet — webview`). Chrome ` — app` spawned a new window every click. Replaced with a real WKWebView app so the Dock shows a running-dot and a second click focuses the same window (GitHub.app pattern)
- **AFC** `Grok` 2026-09-01 — IN PROGRESS — Dock launcher for local DSH web (branch `grok/dsh-dock-launcher`, worktree `~/apps/fleet — dock`). Always-on `dsh-web` idle ~12 MB / 0% CPU — leave it running. `~/Applications/DeepSeek Harness Web.app` opens Chrome ` — app=http://127.0.0.1:3080/` with no Terminal. Full-bleed square icon (not the official squircle)
- **AFC** `Grok` 2026-09-01 — COMPLETED/MERGED #162 — DSH web :3080 on Tailscale + Shellular Thinking hang (branch `grok/dsh-tailscale-shellular`, worktree `~/apps/fleet — shellular`, board `32dbbf8d`). Web UI default is 127.0.0.1:3080; Tailscale Serve `https://macbook.boa-roygbiv.ts.net:3080`. Shellular listed sessions then hung on Thinking because headless dsh is silent until the final answer
- **AFC** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #159 — fleet adoption standing split + CI/ship hygiene (branch ` -fleet-adoption`, worktree `~/apps/fleet — adopt`, board `42c563a6`). Implementation of the 2026-09-01 adoption report: Personal-Site Datadog-only, no — project for CTS/fleet-ops, Android deferred, Seer gated to ST+CT, overlap table, CI fingerprints `[app, work
- **AFC** `Grok` `Sentry` 2026-09-01 — COMPLETED/MERGED #158 — sponsored-account fleet integration plan (branch ` -fleet-integration-plan`, worktree `~/apps/fleet — plan`, board `6ac85c0e`). Live inventory of org `jays-services` (8 projects, 0 alert rules, stale crons, ST uptime failing on homepage). Plan: `docs/plans/2026-09-01 — fleet-integration.md`. No runtime changes. Sla
- **AFC** `Claude` 2026-09-01 — IN PR — Canonical `## Never idle-watch a PR` section in `AGENT-SYNC.md` (branch `claude/never-idle-watch-rule`). Owner ruling 2026-09-01: agents "should never just wait and watch for things to merge since that wastes tokens/time and they inevitably almost invariably end up slowly wasting money/quota while the PR sits there with conflicts or comments/issues unresolved."
- **AFC** `Grok` `Claude` `Cursor` `Codex` `Gemini` 2026-09-01 — IN PROGRESS — Mine chat logs + extra markdown into fleet-agents RAG. Board `ef4df7cb`. Claimed Tue, Sep 1, 2026. Worktree `~/apps/fleet — mine` @ `grok/rag-mine-chats-docs`. AFC #170. Staging `~/apps/fleet-rag/mined/`: — 7224, — 36783, — 1164, — 555, — 4446, Kimi 18, BotFleet 148, extra markdown 2158, distilled lessons 4012 (75k JSONL
- **AFC** `Grok` 2026-09-01 — IN PROGRESS — Fleet RAG on every device (`grok/fleet-rag-everywhere`). Board `c03d33a2`. REST `/recall/stats|search|contribute` on seat-mcp + public hop `agents.jays.services`. MCP tools already live. Owner: all agents all platforms
- **AFC** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — Add fleet — ci-report.yml + scripts/sentry-ci-report.py (branch ` -ci-report`, worktree `~/apps/fleet — ci`, board `6758a621`). Gold copy UM PR #1394. APP=`ai-fleet-coordinator`. Fingerprint `[ci-failure, ai-fleet-coordinator, workflow]`. <! — wb-agent-report:6758a621 — >
- **AFC** `Grok` `Sentry` 2026-09-01 — IN PROGRESS — org extras: detector-scoped PD, uptime, dashboard, metric alerts (` -org-rollout`). Board `31bd2e3a`. Worktree `~/apps/fleet — org`. PD test page #86 resolved. Workflow `3930764` uses `detector_ids`. Dashboard `9917821`. Rollout `docs/rollouts/2026-09-01 — org-rollout.md`

## 2026-08-31

*0 PRs merged · 0 issues opened · 0 issues closed · 18 effort rows*

### Effort board

- **CT** `Claude` `Grok` 2026-09-05 — ( usage-cap pickup) — LANDED — Full-stack audit report + effort-log hygiene (board `f74642d0`, branch ` -handoff-hygiene`). — hit its usage cap with the 2026-08-31 audit (`docs/audits/2026-08-31-full-stack-audit.md`) staged in `~/apps/congress — audit` but never committed, and six already-merged PRs (#2301, #2303, #2304, #2305, #2306, #2313, #
- **CT** `Antigravity` 2026-08-31 — COMPLETED/DEPLOYED #2271 (`c2fd4ded`) — Add iOS Beta / TestFlight links across website and /beta redirect routes (branch `antigravity/ios-beta-testflight-link`). Added direct links to the iOS Beta / TestFlight app across high-visibility surfaces on the website: site footer (`<footer class="site-footer">`), Delivery tab push notifications card (`subsPush`), mobile signed-out h
- **CT** `Antigravity` 2026-08-31 — COMPLETED/DEPLOYED #2269 (`0e9fd7e8`) — Review queue audit, filing reconciliation, 50MB raw limit, and base64 Senate paper OCR (branch `antigravity/filing-recovery-and-size-limit`). Audited all rejected/failed filings and conducted 10%+ spot check across August 2026 filings against source PDFs/HTML. Fixed `H-2026-9116311` (Rep. Hal Rogers handwritten PTR) to honest `verified_
- **CT** `Antigravity` 2026-08-31 — COMPLETED/DEPLOYED #2267 (`ffa6edf2`) — Rebalance Trends layout, unify KPI font sizes, center disclosure metrics, and polish auth modal (branch `antigravity/trends-layout-kpi-auth-polish`). Constrained Trends container to centered `1280px` max-width, symmetrically paired cards into 2-column grids (Top Performers + Most Active Politicians, By Party + By Asset Type), moved Buys
- **CT** `Claude` 2026-08-31 — IN PROGRESS - B2 prune delete-mechanism fix + bulk/ lifecycle 14d->7d (branch `claude/b2-prune-deletefile-fix`). First live prune tick (12:15Z) selected candidates correctly but deleted 0: `rclone deletefile` cannot resolve exact paths under the scoped writer key ("is a directory or doesn't exist" while `lsf` lists it). Fix: anchored `rclone delete — include` + re-list
- **CT** `Claude` 2026-08-31 — COMPLETED/DEPLOYED-TO-HOST #2264 (`1646679f`) — B2 hetzner/ snapshot prune + R2 weekly receipt guard (branch `claude/b2-hetzner-prune-weekly-guard`). Merged 11:20Z (`typecheck + test` green); installed on fleet-hetzner-nbg1 at 11:22Z as `/usr/local/sbin/fleet-sqlite-backup.sh` (backup at `/root/fleet-sqlite-backup.sh.pre-prune-1788175363`; host `bash -n` clean; host-loca
- **CT** `Claude` 2026-08-31 — COMPLETED/DEPLOYED #2262 (`8081e726`) — latency_probes stops paging config-retired providers (board `c3fb117a`, branch `claude/latency-health-retired-providers`). Verified live 2026-08-31 08:41Z (~9 min after merge): `/api/health/latency` 200 with "Latency probes live … across 1 provider(s); retired in config (not paged): quiver, unusual_whales"; UptimeRobot monitor 8037
- **UM** `Grok` `Claude` 2026-08-31 — IN PR #1420, adopted and landed by — Top-to-bottom full-stack audit (web all sizes, iOS Client+Local, backend ingest/money/ops). Branch `grok/full-stack-audit`, worktree `~/apps/usage — audit`, board `da6edf84`. Read-only team review; no product changes. Report: `docs/audits/2026-08-31-full-stack-audit.md`. `AGENTS.md` daily-rollups exclusion note corrected
- **UM** `Antigravity` `Sentry` 2026-08-31 — COMPLETED (merged to `main`) — observability expansion: Session Replay, trace sampling, — Crons, and fleet health integration (PR #1388). Expands — observability in Usage-Monitor utilizing the fleet's $5,000 credit sponsored tier: enabled masked Session Replay by default on web client (`replaysOnErrorSampleRate: 1.0`, `replaysSessionSampleRate: 0.1`
- **UM** `Claude` 2026-08-31 — COMPLETED/MERGED #1386 `8ca36aff` — Three collectors had a main guard that silently no-ops on paths with spaces (branch `claude/collector-main-guard-hardening`, worktree `~/apps/usage — ci-drift`). #1383 said its bare-filename guard was the only bad one in `scripts/`; true as written, but an audit of all four entrypoint idioms found three more. ` -usage-collect
- **UM** `Claude` 2026-08-31 — COMPLETED/MERGED #1381 `ab68c2d8` — CI verify-job drift: wire the last three offline `test:` scripts (branch `claude/ci-verify-drift-three-tests`, worktree `~/apps/usage — ci-drift`, board `cd0855dc`). `npm run verify` runs fourteen gates; `.github/workflows/ci.yml`'s `verify` job ran eleven. `test:session-token-collectors`, `test:cf-token-map`, and `test:replica
- **UM** `Claude` 2026-08-31 — COMPLETED/MERGED #1373 `872b498f` — iOS UI polish batch + R2 ghost-bucket fix + infra investigations (branch `claude/ios-ui-polish-and-infra-invest`, worktree `~/apps/usage- `, board `9f03f6d8`, completed). iOS: anchored full-width mostly-solid tab bar (no capsule gaps), de-duplicated `tabBarScrollClearance` (7 feature roots stacked a second 96pt+96pt application
- **DD** `Grok` 2026-08-31 — COMPLETED - Full-stack audit of web (all sizes), iOS, Android, and backend. Branch `grok/full-stack-audit`, worktree `~/apps/dealdex — audit`. Owner-requested top-to-bottom review/report. <! — wb-agent-report:053cdba545734d218011bf7022df21fd — >
- **DD** `Antigravity` `Sentry` 2026-08-31 — COMPLETED (merged to `main`) — client observability: Session Replay, error capture & distributed tracing (PR #217). Integrated `@sentry/react` client error monitoring, Session Replay (100% on error, 10% baseline session, privacy-masked), and distributed browser tracing in `src/lib/observability/sentry.ts` and `src/routes/__root.tsx`. Gated on `VITE_SENTRY_DSN`
- **DD** 2026-08-31 - BF-FIXER - COMPLETED - Remove scanner intro and keep marketplace toggles on one mobile row. <! — wb-agent-report:128f1e71638c46dd8327235b8fcecd66 — >
- **PS** `Antigravity` 2026-08-31 — COMPLETED — Add TestFlight Public Beta links across all fleet apps (branch `ag/testflight-links`). Added TestFlight badges to project cards and created dedicated TestFlight Public Betas showcase section on `jays.services` for all 10 fleet app beta streams (ContactLogo iOS/macOS, Autorotate iOS/macOS, Socratic Trade iOS, Congress.Trade iOS, Usage Monitor Clien
- **AFC** `Antigravity` `Sentry` 2026-08-31 — COMPLETED / PR OPEN — Fleet — monitor expansion & project provisioning (branch ` -observability-expansion`). Added `dealdex` and `botfleet` to `PROD_HEALTH_ENDPOINTS` with JSON/HTTP response detection, added PM2 tags, and provisioned — projects `botfleet`, `autorotate`, and `contactlogo` under org `jays-services`. Rollout: `docs/rollouts/2026-08-31-fleet-se
- **AFC** `Claude` 2026-08-31 — DEPLOYED — Self-hosted bge-m3 embeddings + `fleet-agents` Qdrant collection. Board `7dbd6228`. Worktree `~/apps/fleet — embeddings` @ `claude/local-embeddings-fleet-rag`. Coolify service `tei-bge-m3` (`cday9viyj6mwlfr8egnoknoa`, mesh-only `100.69.77.26:8081`, bearer auth, 6 CPU / 10 GiB) plus collection `fleet-agents` in the existing `qdrant-st` instance (1024-dim

## 2026-08-30

*0 PRs merged · 0 issues opened · 0 issues closed · 2 effort rows*

### Effort board

- **AFC** `Grok` 2026-08-30 — IN PROGRESS — seat-mcp — sessionId flush + one-job queue (`grok/seat-flush`). Board `51965c1b`. Worktree `~/apps/fleet — flush`. Job 401c53c0/15958b82: sessionId none, bytesOut 0, 900s -15. Do not start — leader. Do not extra-ship ST
- **AFC** `Grok` 2026-08-30 — IN PROGRESS — auto-approve permissions + ACP terminals (`grok/acp-auto-approve`). Board `e1dc9024`. Worktree `~/apps/fleet — auto-approve`. Pick offered allow option on `session/request_permission`; implement `terminal/`; acp-home `[ui] permission_mode = always-approve`. Not rebasing ST #3120. Not restarting — leader

## 2026-08-29

*0 PRs merged · 0 issues opened · 0 issues closed · 2 effort rows*

### Effort board

- **CL** `Grok` `Claude` 2026-08-27 — IN PROGRESS — Pickup — PR #24 local compile (board 30af32b2, issue #30, worktree `~/apps/contactlogo — eval` @ `claude/full-app-evaluation-wwwwk1`). Native Swift/Android compiled for the first time. Golden corpus now runs in Swift, TypeScript, and Kotlin. `UIBackgroundModes=processing` is in the built iOS Info.plist. PR #24 merged 2026-08-29. Remaining own
- **AFC** `Grok` 2026-08-29 — IN PROGRESS — Per-session MCP pick for — (`grok/acp-mcp-pick`). Board `1613bd82`. Worktree `~/apps/fleet — mcp-pick`. `opts.mcpServers` names on `seat_launch` — only. — stripped `GROK_HOME`. TUI keeps the full set. No TUI picker

## 2026-08-28

*0 PRs merged · 0 issues opened · 0 issues closed · 2 effort rows*

### Effort board

- **CT** `Antigravity` 2026-08-28 — IN PROGRESS (branch `antigravity/tailscale-residential-proxy`) — Tailscale residential proxy on Mac & server-directed scraping/probing. Deploying a lightweight HTTP/CONNECT proxy on Mac over Tailscale (`100.113.106.39:3128`), retiring local scout in favor of server-directed scraping & latency probes, and adding native proxied fetch in Deno with fail-soft fallback wh
- **DD** `Antigravity` 2026-08-28 — COMPLETED/MERGED #211 (`e64ae0d`) — Fix Datadog 503 / Vercel secrets, PGlite WASM packaging, iOS unmodifiable dealdex.net origin & polished Google/Apple/X sign-in buttons. Configured missing production secrets on Vercel (`DD_API_KEY`, Better Auth, OAuth IDs), added `copy-pglite.mjs` for serverless function WASM assets, made iOS origin unmodifiable to `https://dealdex.n

## 2026-08-27

*0 PRs merged · 0 issues opened · 0 issues closed · 9 effort rows*

### Effort board

- **CT** `Claude` 2026-08-27 — IN PR — Litestream sync-interval 5m -> 15m (branch `claude/litestream-sync-15m`). Owner confirmed all three fleet apps share ONE Backblaze account (caps are fleet-wide) and asked for a frequency reduction. CT is the safe app to coarsen: data is re-ingestable, and 15m cuts quiet-period object count and downstream compaction re-reads 3x. ST deliberately stays at 300s (li
- **CT** `Antigravity` 2026-08-27 — COMPLETED/DEPLOYED #2246 (`946866ea`) — Datadog APM tracing alignment with Socratic.Trade on us5.datadoghq.com (branch `antigravity/datadog-apm-parity`). Added DATADOG_API_KEY and DATADOG_APP_KEY aliases, default site fallback to us5.datadoghq.com, DD_AGENT_HOST / DD_TRACE_AGENT_URL support, npm:dd-trace Deno APM initialization, and HTTP / outbound fetch / queue APM spans. L
- **CT** `Claude` 2026-08-27 — IN PR — Litestream sync-interval 5m -> 15m (branch `claude/litestream-sync-15m`). Owner confirmed all three fleet apps share ONE Backblaze account (caps are fleet-wide) and asked for a frequency reduction. CT is the safe app to coarsen: data is re-ingestable, and 15m cuts quiet-period object count and downstream compaction re-reads 3x. ST deliberately stays at 300s (li
- **CT** `Antigravity` `Grok` 2026-08-27 — COMPLETED/MERGED #2243 (`ae79e816`) — Restore iOS build number format to 1.0.# (timestamp) (branch `antigravity/restore-ios-timestamp-build-number`). Reverted — bot's removal of timestamp in CFBundleVersion (`1.0.81 (1.0.81)` -> `1.0.# (YYYYMMDDHHMM)`). Marketing version stays 1.0.# (`CFBundleShortVersionString`) and UTC timestamp is restored for `CFBundleVersion` so App S
- **CT** `Antigravity` 2026-08-27 — COMPLETED/MERGED #2241 (`b5cb1fd9`) — iOS UI polish across Trends, Directory, Delivery, Filter controls, and Ticker/Politician sheets (branch `antigravity/ios-ui-polish-trends-directory-delivery`). Refined Trends Market Snapshot KPI grid to 3-per-row with responsive 2-per-row fallback (`ViewThatFits`), darkened filter dropdowns & symbols on Trends/Trades (`glyphGrey` = label
- **UM** `Claude` 2026-08-27 — COMPLETED (ops heal, docs PR) — Litestream B2 L0 corrupt-object heal. Post-#1368 the retry storm persisted: deterministic `close reader 14: file checksum mismatch` = corrupt L0 `26855`; every ~30-60s retry re-read 5,557 L0 objects (~1 GB) from B2 for ~2.2 days — the shared Backblaze daily-cap burn. Deleted 4,994 objects wholly below the newest L9 snapshot boundary `27bc
- **UM** `Claude` 2026-08-27 — IN PR — Litestream B2 multipart fix: part-size 10MB + concurrency 2 (branch `claude/litestream-b2-part-size`). L1 compaction against B2 was wedged in a retry storm (119 "compaction failed" checksum-mismatch multiparts in ~2h on 2026-08-27), burning the shared Backblaze daily transaction caps. Mirrors Socratic.Trade's proven 2026-08-07/22 fix. YAML-only. Rollout: `docs
- **AFC** `Grok` 2026-08-27 — IN PROGRESS — TUI drive follow-ups + cloud hop (`grok/tui-drive-cloudhop`). Board `56cc91fd`. Worktree `~/apps/fleet — cloudhop`. Install-on-merge, await-next-turn, pendingTool, self-guard, tracked seat-mcp launchers, cloud MCP hop `agents.jays.services`. Generic any-seat
- **AFC** `Grok` `Cursor` 2026-08-27 — IN PROGRESS — Bot drive for live — TUI sessions (`grok/tui-drive`). Board `d854b8b4`. Worktree `~/apps/fleet — drive`. leader-client `prompt`/`peek`, ` .py`, seat-mcp v1.1 `grok_sessions_list`/`grok_session_prompt`, skill `drive — tui` (GB + ). Handshake ok; list 30 sessions / 2 live. Did not inject a test prompt into the live TUI

## 2026-08-26

*0 PRs merged · 0 issues opened · 0 issues closed · 16 effort rows*

### Effort board

- **CT** `Grok` 2026-08-26 — IN PR — Publisher drain of 3 terminal review-queue rows + self-close pipeline (issue #2230, board `3390fd23`, branch `grok/review-queue-terminal`, worktree `~/apps/congress — terminal`). Live: confirmed Cohen `H-2026-20035235` (2 official buys); rejected Hern `H-2026-20035196` as later official amendment of persisted `H-2026-20035134`; rejected Rogers `H-2026-911
- **CT** `Antigravity` 2026-08-26 — COMPLETED / IN PR (branch `antigravity/update-asc-release-checklist`) — Update App Store release checklist with live ASC review status and merged features. Updated CHECKLIST_FOR_ASC_PUBLIC_RELEASE.md to reflect the live ASC status as of Aug 26, 2026 (submission `b174dd86` state UNRESOLVED_ISSUES / version 1.0.81 REJECTED), documented Apple review feedback on Guidelines 2.1(a)
- **CT** `Antigravity` 2026-08-26 — COMPLETED (branch `antigravity/admin-auth-and-probe-intervals`) — Streamline Admin & Review Queue UI, Government Poll Interval Brackets, and 24h Price Snapshots. Verified session-based admin recognition without secondary login dialogs or browser token popups (`canUseAdmin()` unlocked via `ADMIN_EMAILS` session allowlist). Durably recorded previous check timestamp ($T
- **CT** `Antigravity` 2026-08-26 — COMPLETED — Submit Congress.Trade iOS 1.0.177 with Guideline 2.1(a) and 2.1(b) fixes. Built fresh Tahoe GM binary 202608262138 on GitHub-hosted macos-latest (run 33016281432), updated ASC version 1.0.177, attached build 29d9c081, attached 4 items (version + group 3a37da1c + monthly efbef974 + annual f85b493e), verified physical-device deletion video (COMPLETE)
- **CT** `Antigravity` 2026-08-26 — COMPLETED/MERGED (#2225 `5bd14d30`) — App Store release checklist update. Updated CHECKLIST_FOR_ASC_PUBLIC_RELEASE.md with August 26, 2026 live ASC state, rejected submission b174dd86 summary, and Guideline 2.1(a) / 2.1(b) resolution path
- **UM** `Antigravity` 2026-08-26 — COMPLETED/MERGED #1363 `5d2c580f` — Native iOS Settings-style long-press to copy (branch `ag/ios-long-press-copy`). Implemented system-wide native iOS Settings-style long-press to copy (`CopyableValueModifier`, `.copyableRow(label:value:)`, `.copyableValue(_:label:)`, and `CopyableLabeledContent`) across DesignSystem, Settings, Computers, Agents, Platforms, ServerSt
- **UM** `Antigravity` `Claude` 2026-08-26 — COMPLETED — Comprehensive PR review fixes & thread resolution (branch `antigravity/reviewer-feedback-fixes`). Resolved reviewer feedback across PRs #1352 / #1354 / #1356 / #1357 / #1358 / #1360: included retained rollups from `ExternalUsageEventDailyRollup` in All Time agent aggregations, preserved the — `service= -code` discriminator, reconciled 5h b
- **DD** `Cursor` 2026-08-26 — COMPLETED - DealDex AGENTS hosting copy + land open-redirect #199. <! — wb-agent-report:282e1ab0f563489581129391f7bb1306 — >
- **DD** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Updated `vercel.json` with immutable 1-year cache-control headers for static build assets (`/assets/(.)`), stale-while-revalidate caching for media/fonts/favicons, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), clean URLs, and t
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Updated `site/vercel.json` with `ignoreCommand` to skip redundant builds on non-site repo edits, immutable 1-year cache headers for build assets, media/font cache-control headers, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), cl
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Add PERSONALSITE_DD_ prefixed key support and sync all app Datadog secrets into Infisical shared workspace (branch ag/infisical-prefixed-keys). Wired PERSONALSITE_DD_ key fallbacks in fail-closed.ts and vite.config.ts. Synchronized Datadog secrets for Personal-Site, ContactLogo, DealDex, and Autorotate into shared-at-ct Infisical workspace
- **PS** `Antigravity` 2026-08-26 — COMPLETED — Update DealDex logo, add CTS acronym, and fix Datadog production deployment (branch ag/dealdex-logo-future-dates-prod-fix). Replaced DealDex app icon with official 1024px icon. Added CTS acronym fallback for Congress Trading Shared. Fixed assertDatadogKeysOrThrow to prevent aborting Vercel production build when DD_ are unset
- **AR** `Claude` 2026-08-27 — COMPLETED — Full-field security & quality audit remediation (AR-01…AR-35). Reviewed all five surfaces (web front/back, AutorotateCore, iOS, macOS, Android) against the zero-plaintext / hash-chained-audit / capability-matrix invariants; documented 35 findings in `docs/AUDIT-2026-08-26.md` (PR [#76](https://github.com/jaywedgeworth22/Autorotate/pull/76)) and remedia
- **AR** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Created `apps/web/vercel.json` with Vite framework preset, 1-year immutable cache headers for build assets (`/assets/(.)`), stale-while-revalidate headers for static media/fonts, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), cl
- **CL** `Antigravity` 2026-08-26 — COMPLETED — Add Vercel free feature optimizations (branch `antigravity/vercel-optimizations`). Created `web/vercel.json` with Vite framework preset, 1-year immutable cache headers for build assets (`/assets/(.)`), stale-while-revalidate headers for static media/fonts, strict security headers (nosniff, sameorigin, referrer-policy, permissions-policy), clean U
- **AFC** `Antigravity` 2026-08-26 — DEPLOYED/MERGED #123 — Audit and resolve reviewer comments across past 2 weeks. Claimed Wed, Aug 26, 2026. Fixed mac-auto-cleanup worktree idle/clean checks and agent-sync runtime preservation (#122), dsh-acp watchdog timeout, session/load resume, supported mode restriction (#110, #111), cursor_acp_cloud_bridge authMethods and follow-up response wait (#75), and regis

## 2026-08-25

*0 PRs merged · 0 issues opened · 0 issues closed · 29 effort rows*

### Effort board

- **CT** `Cursor` 2026-08-26 — IN PR — Docs: provider-missing stub auto-close after #2221 (branch `cursor/docs-provider-missing-stub-close`). #2221 landed the live observation reject; July 22 rollout and B6 still described create-only / backlog. Added `docs/rollouts/2026-08-25-provider-missing-stub-close.md` (match order, persisted-only close, no historic sweep, operator SQL). Pointed July 22 follow
- **CT** `Cursor` 2026-08-25 — IN PR — iOS ASC 2.1(a)/(b): login responsiveness + IAP purchase errors (branch `cursor/ios-asc-login-iap-fixes-b12e`). Reviewer iPad Air 11-inch: Sign in with Apple looked hung (no progress/disable); Premium purchase errors used post-charge redeem copy before Apple charged. `SignInPanel` now shows Apple/Google busy state + inline notices; `PremiumPricing.purchaseFailure
- **CT** `Cursor` 2026-08-25 — IN PR — Prod session admin allowlist investigation (branch `cursor/admin-emails-env-investigation-7267`). Live `GET /auth/me` → `admin.allowed:false` for signed-in operator after #2219 removed token UI. Code path (`identity.ts` / `parseEmailAllowlist` / `isAdminSessionEmail`) correct. Infisical congress-trade prod key `ADMIN_EMAILS` present but stale (19-char value ≠
- **CT** `Cursor` 2026-08-25 — COMPLETED/MERGED #2219 — Email-only admin + review_queue publisher webhook (branch `cursor/email-admin-review-notify-b7ee`). Removed public Admin Sign-In / token UI from web (`dashboardHtml.ts`); admin gated on `ME.admin.allowed` (session email on `ADMIN_EMAILS` or persisted grant). `ADMIN_TOKEN` stays server-side only. Added fail-closed signed `REVIEW_QUEUE_PUBLISHER_
- **CT** `Cursor` 2026-08-25 — COMPLETED/MERGED #2221 — Auto-reject provider-missing stubs when official filing is persisted (branch `cursor/provider-missing-stub-close-77a0`). FMP latency can open `provider-missing-` review rows before Senate/House discovery lands; when `S-{uuid}` / `H — {id}` (or matching `source_url`) is already `persisted`, the stub now rejects as duplicate on the next provider o
- **CT** `Cursor` 2026-08-25 — IN PR #2212 — Copy pinned AppUpdatePrompt.swift into the Congress.Trade iOS target (branch `cursor/appupdateprompt-file-8688`). Stop inlining the type in `App.swift`. Real file copied from `scripts/ios-fleet/AppUpdatePrompt.swift`. `knownAppleIds` (stale `online.dealdex`) removed from Swift; live DealDex is `net.dealdex` appleId `6802474288` in `apps.json`. Pin kept
- **CT** `Cursor` 2026-08-25 — IN PR — ios-ship: drop `secrets.` from job/step `if` (DealDex #175 class, branch `cursor/ios-ship-secrets-if-0efe`). After #2207/#2209, `ios-ship` is a 0-job fail: GitHub rejects `if: && secrets.ASC_KEY_ID != ''` (`Unrecognized named-value: 'secrets'`). Keep the scheduled ship gate. Map existing team secrets into step env, check `ASC_KEY_ID` there, then run `ios-a
- **CT** `Cursor` 2026-08-25 — IN PR #2210 — Datadog logs + APM + public RUM on the existing account (branch `cursor/datadog-logs-apm-rum-3c8e`). Deno agentless HTTP intake for logs/APM; RUM via `%GA_SCRIPT%` on public HTML. Reuses fleet `DD_API_KEY` / `DD_APP_KEY` / `DD_SITE` plus RUM client-token aliases. Fail closed / no-op on missing or partial keys. No new Datadog plan, no session replay, no D
- **CT** `Cursor` 2026-08-25 — IN PR — iOS inbound trade/member/ticker links + Trends 5xx retry (audit F1/F4, branch `cursor/ios-deeplink-trends-retry-50f4`). `AppDeepLink` parses `https://congress.trade/?trade|member|ticker=` and `congresstrade://` equivalents; `onContinueUserActivity` for Universal Links; missing/unknown queries stay nil; inbound 404 uses the web not-found copy. Trends reuses the T
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1359 — Fix iOS Swift package test unwraps (branch `fix/ios-swift-test-unwraps`). Extracted `store.listProviders()` out of `XCTUnwrap` autoclosure and fixed optional Double literal comparisons in `LocalConnectAccountsTests.swift` and `OfflineCacheTests.swift`
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1358 — Namecheap adapter, App icon favicon, Twilio SMS gateway, Hetzner watcher & Global Compact Density (branch `ag/namecheap-favicon-hetzner-twilio`). Added Namecheap poll adapter (`src/lib/adapters/namecheap.ts`) and AI agent CLI (`scripts/namecheap.py`) for balance, auto-renew, and domain inventory. Replaced web favicon with multi-resolution R
- **UM** `Antigravity` 2026-08-25 — COMPLETED/MERGED #1357 — Mac Host telemetry parity & dedicated Agents tab (branch `ag/agents-tab-and-mac-parity`). Upgraded Mac watchdog to report dynamic Apple Silicon chip (`Apple M5`), accurate APFS data volume disk usage, Tailscale hostname formatting, grey Not Enabled badges without false alert flags, and full fleet PM2/launchd process monitoring. Added dedica
- **UM** `Cursor` 2026-08-25 — IN PR — Widget topics Mac, Alerts, Providers + dedicated Mac/Alerts tiles (branch `cursor/widget-mac-alerts-providers-ef6c`). Same `services.jays.usage.client.monitor.widget` bundle. Edit Widget lists Budget, LLM Quotas, Servers, Mac, Alerts, Providers. Mac is Computers heartbeat, not Servers → Host. Dedicated Mac (CPU/memory/disk) and Alerts (open list) tiles. Snaps
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1349 `ebcc972` — Usage Monitor widget topics Budget / LLM Quotas / Servers + Large (branch `cursor/widget-topics-737e`). Existing `services.jays.usage.client.monitor.widget` only. Edit Widget picks topic. Snapshot cache extended for LLM + server tiles. Honest empty/stale. No new ASC app
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1347 `258e790` — Pin AppUpdatePrompt.swift for both iOS targets (branch `cursor/appupdateprompt-pin-c60e`). One in-repo ios-fleet pin, copied into App + LocalApp. knownAppleIds off Swift (stale online.dealdex) into apps.json. Live DealDex is net.dealdex appleId 6802474288. No Swift package. testers.json untouched. No ` — force-ship`. LocalUsageMoni
- **UM** `Cursor` 2026-08-25 — COMPLETED/MERGED #1341 `d563c8b` — Datadog logs + APM + gated RUM (branch `cursor/datadog-logs-apm-rum-802c`). Existing US5 account only. No new Datadog spend. Fail closed without `DD_SERVICE`. RUM stays dark until the public pair is set. Sentry/PD stay. Do not promote Coolify until Infisical has `DD_SERVICE=usage-monitor` plus `DD_ENV`/`DD_SITE`/`DD_AGENT_HOST`/`DD
- **UM** `Grok` 2026-08-25 — COMPLETED/MERGED #1343 — Hosted ios-ship ASC import (branch `cursor/ios-hosted-asc-import-1a3f`). Run 32795404598 failed: macos-latest has no `~/.secrets/appstore-connect.env`. Import existing team secrets (ASC_KEY_ID / ASC_ISSUER_ID / ASC_KEY_P8 / IOS_DIST_P12_BASE64 / IOS_DIST_P12_PASSWORD) via `ios-appstore-gm-prepare.sh`, same path as ST #3089. Cache `~/.cache/ios-fl
- **DD** `Antigravity` 2026-08-25 — COMPLETED — Configure Google/Apple/X OAuth from secrets & polish Scan UI button layout. Branch `ag/auth-and-scan-ui-polish`, worktree `~/apps/dealdex- `
- **PS** `Antigravity` 2026-08-25 — COMPLETED — Project domains, hyperlinks, GitHub card buttons (branch ag/project-cards-and-domain-links). Formatted project domains (DealDex.net, Autorotate.Codes, Congress.Trade, SocraticTrade.com, ContactLogo.com, usage.jays.services). Rendered domains in project descriptions as un-underlined blue hyperlinks. Added right-arrow + GitHub action buttons to card header
- **PS** `Antigravity` 2026-08-25 — COMPLETED — Add Autorotate and ContactLogo portfolio work cards (branch ag/portfolio-autorotate-and-contactlogo). Updated site.ts and static/index.html with Autorotate (dynamic secret rotation, native macOS/iOS, ar.png) and ContactLogo. Personal-Site itself excluded from portfolio per owner spec
- **PS** `Cursor` 2026-08-25 — COMPLETED — Designer leftover UX (visitor blurbs + CL/Fleet icons). PR #22. Copy and icons only. Datadog #19 untouched. No deploy
- **PS** `Cursor` `Sentry` 2026-08-25 — COMPLETED — Datadog logs + APM + RUM. PR #19. Existing Datadog account. Fail closed if keys missing. Replay off. — / PagerDuty unchanged
- **AR** `Antigravity` Inline navigation bar title display mode across iOS views — · COMPLETED 2026-08-25. Applied .navigationBarTitleDisplayMode(.inline) to all NavigationStack root and detail views so centered compact title stays pinned during scroll
- **AR** `Cursor` 2026-08-25 — COMPLETED — Pin AppUpdatePrompt.swift from ST fleet, drop knownAppleIds. PR [#75](https://github.com/jaywedgeworth22/Autorotate/pull/75), branch `cursor/app-update-prompt-pin-1b43`. Copy Socratic.Trade `scripts/ios-fleet/AppUpdatePrompt.swift` into `apple/TopSpin-iOS/` (no Swift package). Removed hardcoded `knownAppleIds` (stale `online.dealdex`). Apple IDs com
- **CL** `Antigravity` 2026-08-25 — COMPLETED — Set inline navigation bar title display mode in ContactLogo iOS (branch ag/ios-inline-nav-titles). Set .navigationBarTitleDisplayMode(.inline) on root NavigationStack
- **CL** `Antigravity` 2026-08-25 — COMPLETED — High-res logo sources (Google 256px, Clearbit 512px), quality baseline filter, 404 error prevention, review-first safety refinement, direct card drag-drop upload, and interactive crop/zoom studio modal. Upgraded web candidate sources (Clearbit 512px, Google 256px, Preferred SVGs); prevented SimpleIcons 404 question mark SVGs via strict slug validation; kep
- **AFC** `Cursor` `Antigravity` `Grok` 2026-08-25 — IN PROGRESS — agy-acp session/list wrapper (`cursor/agy-acp-session-list-2365`). Thin NDJSON proxy so Shellular can list — sessions. Does not rewrite agy-acp. Does not change `start.sh` / `:8765`. Keepouts: agents.json, — acp, launchd
- **AFC** `Cursor` `Grok` 2026-08-25 — COMPLETED — Harden pm2 agy-acp fail-closed (`cursor/agy-acp-fail-closed-387d`, #117). Track turbo.sh; start.sh child is turbo; grace 300s; bind persist via `bind-loopback.cjs`. Keepouts: — acp, Shellular agents.json, session scanner
- **AFC** `Grok` `Cursor` 2026-08-20 — IN PROGRESS — 5-day Mac takeover (through 2026-08-25). Owner: this Mac — TUI takes the — queue. — Bot.app is — (`com.anysphere.sand`) and only launches — cloud agents; local chats already sit on ` `. No — cloud from this seat unless owner asks. Board `c8d325b9`. 2h babysit loop. PR conflicts/CI/comments across ST/CT
