

import pytest

from fanfic.models import MetadataHTML


@pytest.mark.parametrize('html,fields', [

    (

        '''
<div id="profile_top" style="min-height:112px;"><span style="cursor:pointer;" title="Click for Larger Image" onclick="var t = $('#img_large img');t.prop('src',t.attr('data-original'));$('#img_large').modal();"><img class="cimage " style="clear:left;float:left;margin-right:3px;padding:2px;border:1px solid #ccc;-moz-border-radius:2px;-webkit-border-radius:2px;" src="//ffcdn2012t-fictionpressllc.netdna-ssl.com/image/3636437/75/" width="75" height="100"></span><button class="btn pull-right icon-heart" type="button" onclick='$("#follow_area").modal();'> Follow/Fav</button><b class="xcontrast_txt">Whispers in the Dark</b>
<span class="xcontrast_txt"><div style="height:5px"></div>By:</span> <a class="xcontrast_txt" href="/u/5880664/IronSparrow99">IronSparrow99</a> <span class="icon-mail-1  xcontrast_txt"></span> <a class="xcontrast_txt" title="Send Private Message" href="https://www.fanfiction.net/pm2/post.php?uid=5880664"></a>
<div style="margin-top:2px" class="xcontrast_txt">There are certain things that are taken for fact in the magical world: the dead cannot return, Dumbledore know and sees all, and, before now, once you've lived thirteen years as one person, you're that person until you die. As I am now finding out, this is not true. And now...I might just be screwed. (AU PoA) *Underwent a title change*</div>
<span class="xgray xcontrast_txt">Rated: <a class="xcontrast_txt" href="https://www.fictionratings.com/" target="rating">Fiction  T</a> - English - Family/Adventure -  Harry P., Ron W., Hermione G., OC - Chapters: 45   - Words: 99,425 - Reviews: <a href="/r/11472121/">89</a> - Favs: 58 - Follows: 84 - Updated: <span data-xutime="1481309053">18m</span> - Published: <span data-xutime="1440631530">8/26/2015</span> - id: 11472121 </span>
</div>
        ''',

        dict(
            title='Whispers in the Dark',
            user_id=5880664,
            username='IronSparrow99',
            summary='There are certain things that are taken for fact in the magical world: the dead cannot return, Dumbledore know and sees all, and, before now, once you\'ve lived thirteen years as one person, you\'re that person until you die. As I am now finding out, this is not true. And now...I might just be screwed. (AU PoA) *Underwent a title change*',
            follows=84,
            favorites=58,
            rating='Fiction T',
            language='English',
            genres='Family/Adventure',
            characters='Harry P., Ron W., Hermione G., OC',
        )

    ),

    (

        '''
<div id="profile_top" style="min-height:112px;"><span style="cursor:pointer;" title="Click for Larger Image" onclick="var t = $('#img_large img');t.prop('src',t.attr('data-original'));$('#img_large').modal();"><img class="cimage " style="clear:left;float:left;margin-right:3px;padding:2px;border:1px solid #ccc;-moz-border-radius:2px;-webkit-border-radius:2px;" src="//ffcdn2012t-fictionpressllc.netdna-ssl.com/image/3368187/75/" width="75" height="100"></span><button class="btn pull-right icon-heart" type="button" onclick='$("#follow_area").modal();'> Follow/Fav</button><b class="xcontrast_txt">Time Turned Back</b>
<span class="xcontrast_txt"><div style="height:5px"></div>By:</span> <a class="xcontrast_txt" href="/u/6892119/TaraSoleil">TaraSoleil</a> <span class="icon-mail-1  xcontrast_txt"></span> <a class="xcontrast_txt" title="Send Private Message" href="https://www.fanfiction.net/pm2/post.php?uid=6892119"></a>
<div style="margin-top:2px" class="xcontrast_txt">Broken &amp; angry after losing Sirius fifth year, Harry recklessly puts himself in harms way, dragging Hermione along for the ride. Now they are stuck in another time with very familiar faces. Will the time spent with lost loved ones help heal Harry or only damage him further? HP/SB with a touch of HG/RL to relieve the overbearing angst.</div>
<span class="xgray xcontrast_txt">Rated: <a class="xcontrast_txt" href="https://www.fictionratings.com/" target="rating">Fiction  T</a> - English - Drama/Angst -  Harry P., Sirius B. - Chapters: 72   - Words: 187,956 - Reviews: <a href="/r/11379661/">449</a> - Favs: 314 - Follows: 516 - Updated: <span data-xutime="1481249615">16h</span> - Published: <span data-xutime="1436878429">7/14/2015</span> - id: 11379661 </span>
</div>
        ''',

        dict(
            title='Time Turned Back',
            user_id=6892119,
            username='TaraSoleil',
            summary='Broken & angry after losing Sirius fifth year, Harry recklessly puts himself in harms way, dragging Hermione along for the ride. Now they are stuck in another time with very familiar faces. Will the time spent with lost loved ones help heal Harry or only damage him further? HP/SB with a touch of HG/RL to relieve the overbearing angst.',
            follows=516,
            favorites=314,
            rating='Fiction T',
            language='English',
            genres='Drama/Angst',
            characters='Harry P., Sirius B.',
        )

    )

])
def test_parse(html, fields):

    html_row = MetadataHTML(html=html)

    row = html_row.parse()

    for key, val in fields.items():
        assert getattr(row, key) == val
