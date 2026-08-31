from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .esewa import generate_signature

import uuid


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'store/product_list.html',
        {'products': products}
    )


def checkout(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        amount = product.price
        tax_amount = 0
        service_charge = 0
        delivery_charge = 0

        total_amount = (
            amount
            + tax_amount
            + service_charge
            + delivery_charge
        )

        transaction_uuid = str(uuid.uuid4())

        signed_field_names = (
            "total_amount,transaction_uuid,product_code"
        )

        message = (
            f"total_amount={total_amount},"
            f"transaction_uuid={transaction_uuid},"
            f"product_code=EPAYTEST"
        )

        signature = generate_signature(message)

        context = {
            "product": product,
            "amount": amount,
            "tax_amount": tax_amount,
            "total_amount": total_amount,
            "transaction_uuid": transaction_uuid,
            "product_service_charge": service_charge,
            "product_delivery_charge": delivery_charge,
            "product_code": "EPAYTEST",
            "signed_field_names": signed_field_names,
            "signature": signature,
        }

        return render(
            request,
            "store/esewa_payment.html",
            context
        )

    return render(
        request,
        "store/checkout.html",
        {"product": product}
    )


def esewa_success(request):
    return render(request, 'store/success.html')


def esewa_failure(request):
    return render(request, 'store/failure.html')