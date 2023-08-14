from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app1.models.tables import Bom, Disti, Unified
import json


def base(request):
    bom = Bom.objects.values()
    disti = Disti.objects.values()
    unified_list = []
    for bom_item in bom:  # 10 5 8
        bom_pn = bom_item["part_number"]
        bom_qty = bom_item["quantity"]
        print(bom_pn, bom_qty)
        print("bom_item", bom_item)
        disti_item = {}
        for item in disti:
            if item["part_number"] == bom_pn:  # first condition
                disti_item.update(item)

        # disti_item = next((item for item in disti if item["part_number"] == bom_pn), None)
        print("dist_item", disti_item)
        if  disti_item:
            disti_pn = disti_item["part_number"]
            disti_qty = disti_item["quantity"]
            error_flag = ""  # No error
            # 15>10
            if disti_qty > bom_qty:
                split_qty, remainder = divmod(disti_qty, bom_qty)
                print("remainder", remainder)
                unified_list.append(
                    {
                        "bom_pn": bom_pn,
                        "bom_qty": bom_qty,
                        "disti_pn": disti_pn,
                        "disti_qty": bom_qty,
                        "error_flag": error_flag,
                    }
                )
                print("23unified", unified_list)
                print(type(unified_list))

                while remainder > 0:
                    #next_bom_item = next(
                       # (item for item in bom if item["part_number"] != bom_pn), None
                    #)
                    next_bom_item=[]
                    for item in bom:
                        if item["part_number"]!=bom_pn:
                            next_bom_item.append(item)
                    print("next_bom_item", next_bom_item)
                    if next_bom_item:
                        # print("next_bom_qty",next_bom_item)
                        next_bom_qty = next_bom_item["quantity"]
                        print("next_bom_qty", next_bom_qty)

                        if remainder >= next_bom_qty:
                            unified_list.append(
                                {
                                    "bom_pn": next_bom_item["part_number"],
                                    "bom_qty": next_bom_qty,
                                    "disti_pn": disti_pn,
                                    "disti_qty": next_bom_qty,
                                    "error_flag": error_flag,
                                }
                            )
                            print("second unified >re", unified_list)
                            remainder -= next_bom_qty
                            next_bom_item["quantity"] = 0
                        else:
                            unified_list.append(
                                {
                                    "bom_pn": next_bom_item["part_number"],
                                    "bom_qty": next_bom_qty,
                                    "disti_pn": disti_pn,
                                    "disti_qty": remainder,
                                    "error_flag": error_flag,
                                }
                            )
                            print("second unified <ree ", unified_list)

                            next_bom_item["quantity"] -= remainder
                            print(next_bom_item)
                            remainder = 0
                    else:
                        break
            else:
                unified_list.append(
                    {
                        "bom_pn": bom_pn,
                        "bom_qty": bom_qty,
                        "disti_pn": "",
                        "disti_qty": "",
                        "error_flag": "Missing in Disti",
                    }
                )
                print("23unified2", unified_list)
        else:
            unified_list.append(
                {
                    "bom_pn": bom_pn,
                    "bom_qty": bom_qty,
                    "disti_pn": "",
                    "disti_qty": "",
                    "error_flag": "Missing in Disti",
                }
            )
            print("firstwrong unifi2", unified_list)

    for disti_item in disti:
        disti_pn = disti_item["part_number"]
        disti_qty = disti_item["quantity"]
        #bom_item = next((item for item in bom if item["part_number"] == disti_pn), None)
        bom_item=[]
        for item in bom:
            if item["part_number"] == disti_pn:
                bom_item.append(item)
                
        if not bom_item:
            unified_list.append(
                {
                    "bom_pn": "",
                    "bom_qty": "",
                    "disti_pn": disti_pn,
                    "disti_qty": disti_qty,
                    "error_flag": "Missing in BoM",
                }
            )
            print("not bom", unified_list)
    # return unified_list
    return render(request, "app1/unifield.html", {"unified_list": unified_list})
    return JsonResponse(list(unified_list), safe=False)

    return JsonResponse(request, list(bom), safe=False)
    return HttpResponse(("thanks for coming "))


# Create your views here.
