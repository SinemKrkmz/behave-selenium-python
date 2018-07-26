from behave import *


use_step_matcher('re')


@then(r'Add "(.*)" product to favorites')
def impl(context, third = "third"):
    context.actionwords.add_third_product_to_favorites(third)


@then(r'I enter search text "(.*)"')
def impl(context, samsung = "Samsung"):
    context.actionwords.i_enter_search_text_samsung(samsung)


@then(r'I click page button "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.i_click_page_button_p1(p1)


@then(r'I click button Üye Girişi')
def impl(context):
    context.actionwords.i_click_button_uye_girisi()


@then(r'delete favorites product')
def impl(context):
    context.actionwords.delete_favorites_product()


@then(r'shown favorites product')
def impl(context):
    context.actionwords.shown_favorites_product()


@then(r'I enter valid password')
def impl(context):
    context.actionwords.i_enter_valid_password()


@then(r'I click link favorites')
def impl(context):
    context.actionwords.i_click_link_favorites()

@then(r'I click favorites product')
def impl(context):
    context.actionwords.i_click_favorites_product()

@then(r'I click link Giriş Yap')
def impl(context):
    context.actionwords.i_click_link_giris_yap()


@then(r'"(.*)" search is shown')
def impl(context, p1 = ""):
    assert context.actionwords.p1_search_is_shown(p1) == p1


@then(r'I click button Search')
def impl(context):
    context.actionwords.i_click_button_search()


@then(r'Second page is shown "(.*)"')
def impl(context, p1=""):
    assert p1 == context.actionwords.second_page_is_shown()


@given(r'got web site "(.*)"')
def impl(context, p1 = ""):
    context.actionwords.got_web_site_p1(p1)


@then(r'product deleted "(.*)"')
def impl(context,p1=""):
    assert  context.actionwords.product_deleted() == True


@then(r'title is shown "(.*)"')
def impl(context, p1=""):
    assert p1 == context.actionwords.title_is_shown()


@when(r'get page title')
def impl(context):
    context.actionwords.get_page_title()


@then(r'I enter  email')
def impl(context):
    context.actionwords.i_enter_email()

@then(r'I click delete tamam button')
def impl(context):
    context.actionwords.i_click_delete_tamam_button()


