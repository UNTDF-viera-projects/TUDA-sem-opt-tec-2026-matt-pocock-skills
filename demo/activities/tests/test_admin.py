from .support import NOW, BaseCase, login_teacher

class AdminTests(BaseCase):
    def test_admin_rejects_capacity_and_read_only_registration(self):
        self.enroll();self.enroll(self.bruno)
        login_teacher(self.client)
        response=self.client.post(f"/admin/activities/activity/{self.activity.pk}/change/", {"title":"Práctica","description":"Datos","starts_at_0":"2030-10-03","starts_at_1":"09:00:00","capacity":1,"is_active":"on","_save":"Guardar"})
        self.assertEqual(response.status_code,200);self.assertContains(response,"No puede reducir")
        self.activity.refresh_from_db();self.assertEqual(self.activity.capacity,2)
        self.assertEqual(self.client.get("/admin/activities/registration/add/").status_code,403)
    def test_admin_shows_cancelled_at_in_list_and_detail(self):
        self.enroll();self.cancel()
        login_teacher(self.client)
        registration=self.activity.registrations.get()
        # NOW en UTC 12:00 se lee 09:00 en Ushuaia.
        expected="1 Oct. 2030 09:00"
        self.assertContains(self.client.get("/admin/activities/registration/"),expected)
        self.assertContains(self.client.get(f"/admin/activities/registration/{registration.pk}/change/"),expected)
    def test_admin_registration_stays_read_only(self):
        self.enroll();self.cancel()
        login_teacher(self.client)
        registration=self.activity.registrations.get()
        url=f"/admin/activities/registration/{registration.pk}/change/"
        self.assertEqual(self.client.get("/admin/activities/registration/add/").status_code,403)
        self.assertEqual(self.client.post(f"/admin/activities/registration/{registration.pk}/delete/").status_code,403)
        self.client.post(url,{"student":self.bruno.pk,"activity":self.activity.pk,"_save":"Guardar"})
        registration.refresh_from_db()
        self.assertEqual(registration.student,self.ana);self.assertEqual(registration.cancelled_at,NOW)
    def test_admin_can_reduce_capacity_after_a_cancellation(self):
        self.enroll();self.enroll(self.bruno);self.cancel(self.bruno)
        login_teacher(self.client)
        response=self.client.post(f"/admin/activities/activity/{self.activity.pk}/change/", {"title":"Práctica","description":"Datos","starts_at_0":"2030-10-03","starts_at_1":"09:00:00","capacity":1,"is_active":"on","_save":"Guardar"})
        self.assertEqual(response.status_code,302)
        self.activity.refresh_from_db();self.assertEqual(self.activity.capacity,1)
