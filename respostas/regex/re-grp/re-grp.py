import re
import datetime

entry = """
Aperiam similique dicta mollitia recusandae optio. Enim fugiat fugit laudantium et laboriosam. Quam sint neque iste eius neque rem. 1538-08-30 perferendis eaque. Ipsa delectus laboriosam. Placeat facere nostrum molestiae inventore cupiditate laudantium. Eaque vel voluptatum reprehenderit ratione fuga. Provident similique unde doloribus. Sapiente illo impedit animi ad hic veniam. Repudiandae illo explicabo iure delectus error quae soluta. Ipsa dicta amet 2048-11-27T08:21 consectetur quis. Delectus eaque quisquam nihil aperiam adipisci deserunt. Officia quibusdam omnis.

Officia error labore labore quod sunt reprehenderit id. Rem aspernatur voluptates corrupti sequi illo nesciunt. Doloremque reprehenderit perferendis 1812-01-19T12:28. Quaerat libero illo consequuntur. 1269-04-01 laborum 1812-01-19T12:28 consectetur error officia. Illo odio reiciendis aliquam dolores. Voluptas quibusdam in 1812-01-19T12:28 vel reiciendis.

Fugit est ducimus rem nulla. Hic nostrum voluptatibus 1586-03-19 officiis. 1178-11-27 explicabo nisi voluptas excepturi. Repellat explicabo commodi provident. Cupiditate provident amet minus laudantium reiciendis suscipit. Dolores ullam 1586-03-19 natus esse quibusdam. Eaque dolore quia quisquam numquam sunt. Aperiam provident nam voluptas provident fugit. Quia illo dolores eum facere facilis quos.

Magnam assumenda odit aspernatur sint est corporis. Labore quia dolor possimus excepturi rerum ipsum voluptates. Aperiam aspernatur mollitia consequuntur. Sequi necessitatibus quidem nostrum aspernatur facilis ea. Rerum vel molestias. Sit fugit ex in accusantium impedit vitae. Eligendi alias odit vero itaque ullam quisquam. Repellendus delectus sint quasi facere veniam eveniet. Sed quasi illo voluptas voluptatem. Dolorem dignissimos culpa possimus explicabo quibusdam minima. Consequatur quam exercitationem consectetur 1344-10-06 aut a.

Optio cumque unde nemo sunt repudiandae ullam. Nostrum 1250-12-23 vitae corporis corrupti repellendus. Occaecati aliquid suscipit deleniti minus amet voluptatibus. Aut vero eos eligendi laudantium facilis maiores. Dignissimos quibusdam totam. Quia incidunt blanditiis a cupiditate harum adipisci. Voluptate velit occaecati. Nesciunt reprehenderit nulla iusto. Cumque esse quas alias consequatur molestiae voluptates. Laudantium cumque veniam nostrum ducimus eveniet. Repellendus eligendi delectus praesentium quos cum rerum. Fugit distinctio modi.

Eaque porro veniam odit odio. Aliquam doloremque quod pariatur aperiam. Quos ducimus tenetur. Est neque voluptate ducimus neque animi modi. Excepturi deleniti eligendi optio excepturi exercitationem. Perspiciatis atque maxime doloremque natus dolor. Commodi doloremque accusamus mollitia quibusdam. Molestias a eveniet debitis.

Eaque libero deserunt consectetur possimus. Magni perferendis fugit asperiores. Illo perspiciatis asperiores perferendis aspernatur tempora 1577-04-06. In quia nostrum iure placeat. Expedita exercitationem reprehenderit quaerat praesentium. Illum recusandae commodi minus a. Libero dolor aliquam officiis porro nobis veritatis. Quisquam cupiditate cupiditate rem 1854-12-06T19:47 optio quasi.

Enim sequi consequuntur ducimus 1305-06-25T07:30+01:30. Veniam consequuntur voluptatum doloremque minima eaque voluptates. Vitae perferendis ducimus. Molestias odit quis cupiditate. Beatae alias itaque culpa repudiandae voluptas nobis. Quidem ut nam odio consectetur voluptatum. Rerum laborum cumque nobis quae. Praesentium recusandae magni cum fugit quod. Eveniet mollitia harum deserunt. Totam iste ab quaerat quae. Doloribus quo nobis et ducimus maiores. Sed quaerat aspernatur nisi.

Illo quisquam architecto recusandae occaecati nihil voluptatum. Modi nostrum officiis quae eaque repellat dolor doloribus. Cum corporis corrupti sunt. Consequuntur rerum molestiae consequatur assumenda unde distinctio. Consequuntur consectetur quia neque nobis provident natus vero. Veritatis ipsam nemo ab sed. Necessitatibus magni officia distinctio nesciunt repellat voluptates. Debitis iure aliquam rerum commodi ipsa consectetur sequi.

Voluptates voluptas assumenda aliquam ullam eveniet. Error doloribus libero soluta rerum doloribus dicta. Voluptatem tempore libero aliquam earum incidunt. Repudiandae nam molestias laboriosam dolore alias quos. Odio ab molestias voluptate voluptatibus provident deserunt vero. Ea ea culpa 1286-02-19T24:59+05:00 optio.
"""

my_birthday = datetime.date(1999, 2, 2)

regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?P<time>T\d{2}:\d{2}:\d{2})?(?P<timeZone>\d:\d)?")

dates = []
DifDates = []

for date in regex.finditer(entry):
  dates.append(datetime.date(int(date.groupdict()['year']), int(date.groupdict()['month']), int(date.groupdict()['day'])))

for date in dates:
    DifDates.append(abs(my_birthday - date))

response = dates[DifDates.index(min(DifDates))]

print(f'A data mais próxima do meu aniversário: {my_birthday} é {response}')