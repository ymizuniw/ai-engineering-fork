import json

a = json.load(open("lectures/02/result_base.json"))
b = json.load(open("lectures/02/result_epochs10.json"))

print("epochs:", a["config"]["num_train_epochs"], "→", b["config"]["num_train_epochs"])
for phase in ["before", "after"]:
    for k in ["format_rate", "content_rate", "both_rate"]:
        print(f"{phase:6} {k:13} {a[phase][k]:.3f} {b[phase][k]:.3f}")
print("退行:", a["regressed"], "→", b["regressed"])
for x, y in zip(a["knowledge"], b["knowledge"]):
    print(x["質問"], "|", x["学習後の分類"], "→", y["学習後の分類"])
