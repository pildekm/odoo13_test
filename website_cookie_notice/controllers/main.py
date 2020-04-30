# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group
# Copyright 2015 Antiun Ingeniería S.L. <http://antiun.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class CookieNotice(http.Controller):

    @http.route("/website_cookie_notice/ok", auth="public", website=True, type='json',methods=['POST'])
    def accept_cookies(self):
        """Stop spamming with cookie banner."""
        http.request.session["accepted_cookies"] = True
        http.request.env['ir.ui.view'].search([
            ('type', '=', 'qweb')
        ]).clear_caches()
        return {'result': 'ok'}

class WebsiteCookie(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        res = super(WebsiteCookie, self).index(**kw)
        print('Cookie pičko')
        values = {'button_name': 'Yes'}
        return request.render('website_cookie_notice.cookiebanner', values)

