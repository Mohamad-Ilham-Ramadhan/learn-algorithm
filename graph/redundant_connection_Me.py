'''
   (graph) leetcode: 684. Redundant Connection (medium)

   In this problem, a tree is an undirected graph that is connected and has no cycles.

   You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

   Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

   

   Example 1:
      1---2
      | /
      3

      Input: edges = [[1,2],[1,3],[2,3]]
      Output: [2,3]

   Example 2:
      2---1---5
      |   |
      3---4

      Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
      Output: [1,4]
   

   Constraints:
      - n == edges.length
      - 3 <= n <= 1000
      - edges[i].length == 2
      - 1 <= ai < bi <= edges.length
      - ai != bi
      - There are no repeated edges.
      - The given graph is connected.

   Related Topics: 
      (Depth-first search) (Breadth-first search) (Union find) (Graph)

   =================================================================== 

   solution by myself 
      using union find with path compression

   leetcode submission
      solution #2
         runtime: 65 ms, beats 87.07%
         memory:  16.89 MB, beats 69.38%
'''

# True algo (tested len(edges) == 1000 ) but time limit exceeded 
def findRedundantConnection(edges): 
   # collect graph
   graph = {} # nodes: {nodes...}
   for [n1, n2] in edges: 
      if n1 not in graph: graph[n1] = set([n2])
      else: graph[n1].add(n2)
      if n2 not in graph: graph[n2] = set([n1])
      else: graph[n2].add(n1)

   # print('graph', graph)
   prospect = set()
   def dfs(prev, current, visited): 
      visited.add(prev)
      # print('prev', prev, 'current', current, visited)
      for next in graph[current]:
         if next == prev: continue
         if next in visited:
            # print('prospect', current,next) 
            if ((current,next) not in prospect or
                  (next,current) not in prospect
               ):
                  prospect.add( (current,next) )
                  prospect.add( (next,current) )
            continue 
         vis = visited.copy()
         dfs(current, next, vis)

   # start traversing
   for node in graph: 
      nexts = graph[node]
      for next in nexts: 
         vis = set() # visited
         # print('START', node)
         dfs(node, next, vis)
   
   # print('prospect', prospect)
   
   for i in range( len(edges)-1, -1, -1): 
      edge = edges[i]
      if (edge[0], edge[1]) in prospect: 
         return edge
      
# using union find with path compression
def solution2(edges): 
   # create parent of every node, initially their parent is itself. 
   n = 0 # max number of node
   for [n1, n2] in edges: n = max(n, n1, n2)
   parent = []
   graph = {}
   for i in range(n+1):
      parent.append(i) 
      graph[i] = []

   # print('parent', parent)
   # print('graph', graph)
   # union find and union join
   result = None
   # e2 = [[1,2],[2,3],[3,4],[1,4],[1,5]] # [1,4]
   for [n1, n2] in edges:
      # print(parent,'\n')
      parentN1, parentN2 = parent[n1], parent[n2]
      # print('n1', n1, 'n2', n2, 'parentN1', parentN1, 'parentN2', parentN2, graph)
      # there is a cycle
      if parentN1 == parentN2: 
         # print('CYCLE')
         result = [n1, n2]
         continue
   
      # if length of component1 is longer than component2 then join component2 into component1
      '''
         24: [20, 17, 3, 14, 6,20,8,23]
   
      '''
      if (len(graph[parentN1])+1) > (len(graph[parentN2])+1): 
         # print('parentN1 > parentN2')
         graph[parentN1].append(parentN2)
         for child in graph[parentN2]: 
            graph[parentN1].append(child)
            parent[child] = parentN1

         # print('before', graph[parentN1])
         graph[parentN2] = []
         parent[parentN2] = parentN1
         # print('after', graph[parentN1], parent[n2])
         # print('parent after', parent, '\n')
      else: 
         graph[parentN2].append(parentN1)

         for child in graph[parentN1]: 
            graph[parentN2].append(child)
            parent[child] = parentN2

         graph[parentN1] = []
         parent[parentN1] = parentN2
	 
   return result
e1 = [[1,5],[1,4],[3,4],[2,3],[1,2]] # [1,2]
'''
   [[1,5],[1,4],[3,4],[2,3],[1,2]] # [1,2]

   5---1----4---3
       \         \
        -------   2
   {
      1: [5,4,2]
      5: [1]
      4: [1,3]
      3: [4,2]
      2: [3,1]
   }
'''
e2 = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],([6,24]),[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]] # [6,24]


'''
   [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[[[8,22]]],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]] # [6,24]

         24-------
         |       | 
  10--5--6--8--------------    
         |       |         |
      3--17--20---         |
         |                 |
         14                |
                           |
                           |        18 
                           |        |
                       16--22--8----15--23
                             |       |     
                             25   12 19--13
                                    \|
                                  2--4--11
                                     | \       12--4--21  
                                  7--9  21
                                     |
                                     1
'''
e3 = [[2,3],[2,5],[1,5],[2,4],[1,4]] # [1,4]
'''
   [[2,3],[2,5],[1,5],[2,4],[1,4]] # [1,4]
   [2,4] [2,5] [1,4]
   1--5---2--3
   |      |
   -------4
   {
      2: {3,5,4}
      4: {2,1}
      3: {2}
      5: {2,1}
      1: {5,4}
   }
'''
e4 = [[400,429],[215,527],[756,892],[798,963],[29,629],[134,711],[136,702],[38,347],[278,515],[724,744],[499,689],[115,882],[283,832],[338,518],[239,508],[413,994],[230,735],[185,953],[459,660],[739,882],[765,777],[231,424],[553,856],[35,369],[820,909],[672,825],[453,798],[690,879],[786,811],[109,332],[463,545],[593,778],[619,713],[25,705],[778,970],[558,597],[408,556],[171,330],[236,784],[65,946],[318,589],[969,991],[110,208],[297,895],[283,901],[537,876],[49,619],[71,966],[84,239],[70,708],[375,812],[638,842],[264,465],[510,579],[62,470],[124,276],[98,376],[33,143],[216,659],[270,631],[742,869],[236,735],[264,989],[552,767],[471,758],[461,967],[650,974],[144,710],[57,998],[320,783],[237,829],[13,899],[498,904],[440,481],[60,364],[277,788],[326,921],[102,408],[82,195],[252,559],[511,806],[258,298],[89,428],[69,821],[213,829],[479,931],[495,975],[259,487],[755,999],[100,526],[735,918],[187,801],[661,783],[530,834],[271,877],[185,460],[504,749],[567,817],[56,800],[786,967],[566,888],[844,934],[535,790],[739,873],[159,246],[607,968],[838,866],[435,862],[205,278],[67,268],[80,711],[2,823],[577,835],[145,221],[293,350],[234,727],[103,945],[458,546],[468,533],[344,763],[714,956],[226,388],[665,774],[409,442],[200,266],[372,632],[320,341],[36,883],[253,457],[165,791],[10,813],[845,887],[360,490],[265,695],[163,947],[532,833],[697,881],[531,673],[399,663],[445,662],[366,455],[312,358],[49,584],[514,744],[162,175],[473,707],[843,891],[392,433],[694,725],[61,623],[189,821],[447,581],[592,840],[250,517],[84,476],[86,543],[621,674],[209,265],[218,220],[411,1000],[726,936],[466,551],[58,238],[532,650],[145,333],[464,670],[349,582],[444,974],[238,364],[506,803],[570,801],[460,671],[600,803],[380,885],[198,427],[794,927],[626,740],[244,900],[366,701],[71,217],[296,992],[77,940],[260,393],[631,682],[54,448],[367,767],[294,412],[405,536],[583,641],[490,748],[622,769],[256,652],[7,448],[3,812],[252,688],[333,969],[57,994],[324,855],[575,667],[37,348],[683,793],[438,684],[116,567],[406,718],[501,541],[33,276],[933,959],[317,983],[133,627],[7,561],[560,625],[681,927],[296,986],[418,422],[135,727],[741,895],[405,996],[644,986],[242,990],[97,596],[94,408],[539,769],[61,93],[852,942],[112,443],[433,522],[865,908],[46,951],[89,540],[293,958],[367,604],[528,879],[68,676],[507,519],[111,703],[867,925],[84,429],[39,852],[582,782],[21,990],[509,643],[551,796],[488,613],[676,858],[599,833],[393,813],[439,839],[130,977],[695,826],[302,572],[17,838],[382,832],[59,734],[143,655],[785,804],[50,352],[302,905],[285,959],[200,857],[35,198],[15,560],[535,567],[181,854],[751,811],[652,952],[226,898],[781,936],[100,478],[210,558],[121,542],[281,317],[331,897],[468,626],[577,810],[156,182],[397,630],[359,691],[420,529],[375,645],[278,579],[383,779],[612,618],[620,823],[547,964],[238,815],[92,485],[903,963],[354,804],[451,754],[471,557],[363,618],[257,775],[204,944],[10,502],[64,716],[636,658],[426,430],[728,987],[137,418],[395,894],[126,387],[398,607],[172,562],[160,850],[655,728],[38,606],[103,127],[415,493],[282,954],[34,321],[818,973],[65,292],[356,590],[177,325],[753,779],[229,764],[619,920],[475,623],[616,805],[21,684],[224,569],[99,486],[45,703],[20,787],[158,899],[144,623],[115,547],[330,437],[450,594],[445,908],[332,966],[50,594],[410,588],[88,356],[193,268],[488,648],[669,767],[259,496],[126,960],[622,766],[25,227],[326,426],[280,350],[793,846],[283,988],[223,525],[240,648],[202,897],[425,767],[585,735],[68,710],[495,934],[498,674],[300,458],[344,840],[199,663],[7,571],[36,781],[140,319],[11,888],[494,519],[23,698],[301,637],[391,774],[420,912],[136,874],[245,587],[106,888],[696,951],[142,264],[610,744],[30,666],[204,848],[129,890],[876,951],[86,573],[450,939],[49,762],[416,704],[466,929],[938,987],[239,287],[135,250],[871,941],[377,893],[524,742],[179,499],[541,943],[76,861],[165,688],[167,753],[586,950],[43,521],[452,803],[52,912],[659,933],[330,770],[433,472],[669,901],[745,838],[118,232],[91,721],[219,360],[651,942],[653,743],[386,543],[14,350],[332,497],[51,984],[81,173],[158,443],[97,172],[175,347],[166,651],[683,914],[247,1000],[471,916],[418,503],[733,816],[783,858],[471,907],[760,780],[262,517],[89,642],[373,662],[395,530],[67,805],[649,966],[304,728],[525,548],[941,993],[919,943],[128,558],[149,826],[221,229],[115,215],[194,996],[718,746],[656,905],[264,551],[58,738],[146,312],[483,676],[729,847],[635,730],[392,932],[405,839],[272,411],[927,963],[782,840],[3,730],[50,740],[802,816],[492,638],[554,830],[29,245],[215,299],[571,597],[86,563],[374,379],[624,713],[214,297],[255,567],[271,833],[17,200],[788,877],[498,752],[679,866],[164,265],[471,612],[456,812],[656,827],[15,99],[66,324],[292,651],[83,694],[43,361],[209,453],[60,122],[40,374],[191,742],[124,180],[508,659],[156,864],[98,992],[133,922],[355,434],[157,316],[143,254],[646,930],[108,481],[67,915],[321,648],[168,837],[380,814],[37,196],[565,891],[96,460],[117,611],[156,431],[516,992],[759,796],[184,236],[302,568],[421,960],[404,807],[591,957],[310,671],[553,789],[293,296],[79,333],[182,512],[204,207],[44,231],[720,824],[829,998],[517,779],[136,295],[42,224],[170,526],[210,601],[577,621],[51,262],[360,718],[45,75],[13,546],[118,402],[435,603],[510,937],[336,700],[781,799],[389,881],[41,386],[177,290],[295,473],[608,767],[192,510],[97,334],[72,298],[129,487],[132,260],[343,722],[489,736],[229,374],[190,591],[440,870],[581,637],[253,811],[78,647],[614,946],[53,503],[377,613],[208,724],[188,675],[192,408],[310,502],[624,652],[441,629],[470,789],[468,925],[524,974],[276,981],[392,822],[146,967],[18,900],[505,854],[722,797],[252,716],[330,935],[1,646],[269,743],[148,965],[236,520],[503,599],[273,574],[418,706],[827,971],[553,828],[747,808],[196,366],[704,846],[510,595],[84,871],[57,723],[59,340],[401,751],[174,477],[254,513],[60,690],[544,833],[47,668],[48,55],[35,771],[290,327],[4,325],[501,644],[342,480],[407,536],[428,822],[419,670],[314,709],[172,241],[525,978],[77,548],[301,841],[74,394],[315,615],[737,859],[250,474],[479,918],[92,677],[326,867],[463,937],[38,389],[378,386],[379,763],[261,281],[379,697],[349,662],[273,384],[365,512],[412,907],[8,109],[263,407],[182,752],[75,792],[41,654],[804,850],[366,997],[390,655],[685,790],[598,769],[163,459],[12,843],[370,654],[311,904],[173,996],[553,982],[729,769],[89,776],[53,640],[358,555],[5,306],[107,617],[8,19],[715,789],[477,664],[768,899],[248,551],[220,693],[469,878],[197,320],[501,540],[707,849],[310,936],[246,404],[423,621],[881,911],[714,876],[24,364],[140,634],[283,917],[233,249],[866,925],[147,842],[145,947],[580,668],[269,808],[102,909],[707,751],[800,885],[694,738],[32,178],[161,187],[828,854],[385,977],[363,409],[875,934],[657,971],[114,903],[131,445],[186,448],[78,721],[224,469],[436,578],[201,880],[227,675],[398,616],[884,931],[41,737],[115,896],[803,961],[165,663],[126,251],[62,816],[120,184],[680,948],[611,978],[509,647],[225,639],[228,445],[550,711],[472,593],[665,936],[711,939],[106,941],[418,976],[63,904],[157,559],[185,641],[692,730],[346,883],[155,929],[126,924],[374,732],[71,380],[120,526],[264,398],[269,362],[126,837],[152,507],[737,902],[99,299],[666,943],[678,730],[86,222],[86,279],[576,767],[47,821],[55,269],[491,923],[780,967],[164,635],[549,773],[150,468],[141,739],[564,932],[182,297],[338,887],[105,632],[449,770],[698,823],[48,786],[83,899],[26,705],[3,949],[9,414],[220,500],[523,844],[154,908],[375,570],[550,929],[456,734],[755,941],[342,759],[170,756],[336,415],[123,565],[417,460],[953,972],[383,677],[121,300],[414,716],[284,357],[589,738],[744,914],[290,940],[86,291],[482,832],[337,980],[105,870],[175,995],[37,646],[223,863],[76,543],[82,664],[446,818],[191,316],[464,845],[267,960],[16,686],[20,135],[101,719],[467,811],[353,496],[328,870],[505,922],[177,204],[138,196],[206,656],[787,795],[138,368],[151,249],[22,643],[25,61],[8,432],[175,335],[648,769],[853,957],[419,912],[332,622],[488,772],[127,548],[718,854],[620,687],[41,404],[455,700],[277,427],[123,673],[37,777],[132,203],[318,489],[339,537],[531,986],[16,877],[211,787],[72,803],[636,699],[404,720],[1,128],[6,492],[803,818],[75,827],[273,550],[684,749],[28,86],[445,705],[481,974],[345,825],[270,708],[149,761],[212,860],[308,594],[731,924],[302,931],[218,431],[151,395],[23,567],[602,876],[14,452],[538,793],[111,831],[575,721],[254,383],[233,554],[149,1000],[139,140],[127,906],[198,660],[537,985],[189,586],[955,963],[804,948],[3,722],[639,823],[629,675],[206,590],[340,863],[645,979],[313,794],[737,872],[371,877],[158,322],[11,685],[337,367],[243,690],[32,235],[40,446],[153,1000],[73,548],[104,844],[454,696],[709,914],[87,252],[345,477],[176,823],[74,274],[761,861],[628,778],[303,733],[235,900],[361,509],[12,324],[32,954],[878,945],[54,746],[808,837],[225,394],[534,985],[70,637],[420,980],[416,559],[802,836],[434,994],[158,482],[169,562],[207,795],[677,928],[286,714],[74,750],[593,785],[171,396],[15,462],[167,183],[381,1000],[231,511],[174,454],[323,520],[90,675],[750,868],[70,819],[380,504],[281,998],[81,435],[95,218],[202,652],[321,605],[288,960],[478,555],[147,571],[351,630],[403,719],[306,929],[36,920],[286,880],[357,365],[27,147],[139,258],[338,631],[486,757],[605,888],[789,889],[348,484],[321,451],[586,657],[830,914],[118,831],[68,809],[636,962],[289,457],[609,951],[248,851],[75,436],[261,785],[353,862],[898,945],[195,900],[141,890],[107,312],[119,321],[125,681],[211,499],[627,691],[324,864],[806,965],[67,997],[410,719],[305,761],[171,845],[647,910],[202,231],[309,856],[373,712],[352,542],[307,528],[56,897],[111,587],[315,928],[192,201],[728,913],[70,403],[341,519],[886,945],[130,388],[596,705],[85,632],[417,835],[329,764],[824,959],[410,894],[735,852],[218,926],[573,658],[113,850],[263,355],[31,849],[495,965],[715,923],[275,656],[7,717],[733,825],[591,922],[22,728],[400,633],[294,565],[257,537],[102,521],[267,397],[161,773],[110,860]] # [102,521]

import time 
start = time.time()
print('RESULT :', findRedundantConnection(e4))
print('runtime :', time.time() - start)