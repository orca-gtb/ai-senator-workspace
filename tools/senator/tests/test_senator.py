import copy, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import senator as S


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.R = S.registry()

    def test_real_registry_is_valid(self):
        self.assertEqual(S.validate(self.R), [])

    def test_module_without_need_is_rejected(self):
        R = copy.deepcopy(self.R); R["modules"][0]["need"] = ""
        self.assertTrue(any("BUILD TO PRODUCE" in e for e in S.validate(R)))

    def test_module_without_evidence_is_rejected(self):
        R = copy.deepcopy(self.R); del R["modules"][0]["evidence"]
        self.assertTrue(any("evidence" in e for e in S.validate(R)))

    def test_cannot_pass_s1_without_greenlight(self):
        R = copy.deepcopy(self.R); p = R["projects"][-1]; p["stage"] = "S2"; p["gates"]["QG0"] = "pending"
        self.assertTrue(any("QG0" in e for e in S.validate(R)))

    def test_published_requires_qg5(self):
        R = copy.deepcopy(self.R); p = R["projects"][1]; p["dates"]["published"] = "2026-11-26"; p["gates"]["QG5"] = "pending"
        self.assertTrue(any("QG5" in e for e in S.validate(R)))

    def test_unknown_property_rejected(self):
        R = copy.deepcopy(self.R); R["projects"][0]["property"] = "zz"
        self.assertTrue(any("tidak terdaftar" in e for e in S.validate(R)))

    def test_over_allocation_rejected(self):
        R = copy.deepcopy(self.R); R["budget"]["allocation"] = {"wh": 0.8, "sk": 0.5}
        self.assertTrue(any("alokasi" in e for e in S.validate(R)))


class MetricsTests(unittest.TestCase):
    def test_lead_time_only_when_dates_known(self):
        R = S.registry(); R["projects"][1]["dates"] = {"research_start": "2026-11-10", "published": "2026-11-27"}
        rows = {r["id"]: r for r in S.project_metrics(R)}
        self.assertEqual(rows["bagration-p2"]["lead_days"], 17)
        self.assertIsNone(rows["bagration-p3"]["lead_days"])

    def test_credit_cost_is_na_until_plan_credits_known(self):
        R = S.registry(); R["budget"]["plan"]["credits_month"] = None; self.assertIsNone(S.credit_cost_idr(R))
        R["budget"]["plan"]["credits_month"] = 100000
        self.assertAlmostEqual(S.credit_cost_idr(R), 22 * 16500 / 100000)

    def test_finance_bridge(self):
        f = S.finance(S.registry())
        self.assertEqual(f["sub_idr"], 363000)
        self.assertEqual(f["gross_needed_idr"], 863000)
        v = {s["rpm_usd"]: s["monetized_views"] for s in f["scenarios"]}
        self.assertAlmostEqual(v[4], 863000 / 16500 / 4 * 1000)


if __name__ == "__main__":
    unittest.main()
