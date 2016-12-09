

import pytest

from fanfic.models import MetadataHTML


@pytest.mark.parametrize('html,fields', [
    (

        '''
<div id="profile_top" style="min-height:112px;"><button class="btn pull-right icon-heart" type="button" onclick='$("#follow_area").modal();'> Follow/Fav</button><b class="xcontrast_txt">The Conservation of Fame</b>
<span class="xcontrast_txt"><div style="height:5px"></div>By:</span> <a class="xcontrast_txt" href="/u/1265079/Lomonaaeren">Lomonaaeren</a> <span class="icon-mail-1  xcontrast_txt"></span> <a class="xcontrast_txt" title="Send Private Message" href="https://www.fanfiction.net/pm2/post.php?uid=1265079"></a>
<div style="margin-top:2px" class="xcontrast_txt">HPDM slash. Harry has peace at last under a spell that keeps people from remembering he's the Chosen One, until Malfoy stumbles through his wards, pursued by mysterious enemies. Harry has to help him, and possibly bring his peace crashing down. COMPLETE.</div>
<span class="xgray xcontrast_txt">Rated: <a class="xcontrast_txt" href="https://www.fictionratings.com/" target="rating">Fiction  M</a> - English - Romance/Drama -  Draco M., Harry P. - Chapters: 19   - Words: 60,015 - Reviews: <a href="/r/7926634/">611</a> - Favs: 904 - Follows: 498 - Updated: <span data-xutime="1481087877">12/6</span> - Published: <span data-xutime="1331829125">3/15/2012</span> - Status: Complete - id: 7926634 </span>
</div>
        ''',

        dict(
            title='The Conservation of Fame',
            user_id=1265079,
            username='Lomonaaeren',
            summary='HPDM slash. Harry has peace at last under a spell that keeps people from remembering he\'s the Chosen One, until Malfoy stumbles through his wards, pursued by mysterious enemies. Harry has to help him, and possibly bring his peace crashing down. COMPLETE.',
            follows=498,
            favorites=904,
            rating='Fiction M',
            language='English',
            genres='Romance/Drama',
            characters='Draco M., Harry P.',
        )

    ),
])
def test_parse(html, fields):

    html_row = MetadataHTML(book_id=1, html=html)

    row = html_row.parse()

    for key, val in fields.items():
        assert getattr(row, key) == val
